import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import cohere
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
from auth import AuthManager

load_dotenv() ## load all our environment variables

# Initialize Cohere client
co = cohere.Client(os.getenv("COHERE_API_KEY"))

# Initialize Auth Manager
auth_manager = AuthManager()

def get_cohere_response(input_text):
    response = co.generate(
        model='command',
        prompt=input_text,
        max_tokens=1000,
        temperature=0.7,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE'
    )
    return response.generations[0].text.strip()

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template
input_prompt="""
You are a skilled ATS (Application Tracking System) with deep understanding of tech fields, software engineering, data science, data analysis, and big data engineering. 

Your task is to evaluate the resume based on the given job description and provide a JSON response.

Resume: {text}
Job Description: {jd}

Analyze the resume against the job description and provide your response in the following JSON format ONLY:

{{
    "JD Match": "85%",
    "MissingKeywords": ["keyword1", "keyword2", "keyword3"],
    "Profile Summary": "A comprehensive summary of the candidate's profile, skills, and experience relevant to the job description."
}}

Important:
- JD Match should be a percentage as a string (e.g., "85%")
- MissingKeywords should be an array of strings
- Profile Summary should be a single string
- Return ONLY the JSON object, no additional text or formatting
- Ensure the JSON is valid and properly formatted
"""

def show_authentication_page():
    """Show authentication page with login and signup options"""
    st.title("🎯 Smart Resume ATS")
    st.markdown("### Welcome to the Resume Analysis System")
    
    # Initialize session state for showing login/signup
    if 'show_login' not in st.session_state:
        st.session_state.show_login = True
    
    # Create tabs for login and signup
    tab1, tab2 = st.tabs(["🔐 Login", "📝 Sign Up"])
    
    with tab1:
        auth_manager.show_login_form()
    
    with tab2:
        auth_manager.show_signup_form()
    
    # Add some information about the app
    st.markdown("---")
    st.markdown("""
    ### About This Application
    
    This sophisticated ATS project, developed with Cohere AI and Streamlit, seamlessly incorporates advanced features including:
    
    - **Resume Match Percentage**: Get an accurate percentage match with job descriptions
    - **Keyword Analysis**: Identify missing keywords to improve your resume
    - **Profile Summary**: Receive comprehensive profile summaries
    - **User Authentication**: Secure login system to save your analysis history
    
    **Technologies Used:**
    - [Streamlit](https://streamlit.io/) - Web application framework
    - [Cohere AI](https://cohere.ai/) - AI-powered text analysis
    - SQLite Database - Secure user credential storage
    """)

def show_main_application():
    """Show the main resume analysis application"""
    user = auth_manager.get_current_user()
    
    # Sidebar navigation
    st.sidebar.title("Smart ATS for Resumes")
    
    # User info in sidebar
    st.sidebar.markdown(f"👤 **Logged in as:** {user['username']}")
    if st.sidebar.button("🚪 Logout"):
        auth_manager.logout()
    
    st.sidebar.markdown("---")
    
    # Main navigation
    page = st.sidebar.radio("Navigation", [
        "Resume Analysis", 
        "Analysis Results", 
        "Resume Improvement Tips", 
        "Detailed Improvement Plan",
        "User Profile"
    ])

    st.sidebar.subheader("About")
    st.sidebar.write("This sophisticated ATS project, developed with Cohere AI and Streamlit, seamlessly incorporates advanced features including resume match percentage, keyword analysis to identify missing criteria, and the generation of comprehensive profile summaries, enhancing the efficiency and precision of the candidate evaluation process for discerning talent acquisition professionals.")

    st.sidebar.markdown("""
    - [Streamlit](https://streamlit.io/)
    - [Cohere AI](https://cohere.ai/)
    - [Cohere API](https://cohere.ai/api)
    - [Github](https://github.com/praj2408/End-To-End-Resume-ATS-Tracking-LLM-Project-With-Google-Gemini-Pro) Repository
    """)

    add_vertical_space(2)
    st.sidebar.write("Made with ❤ by Bhoomika Vishwanath.")

    # Store the analysis results in session state
    if 'analysis_results' not in st.session_state:
        st.session_state.analysis_results = None

    if 'detailed_improvement_plan' not in st.session_state:
        st.session_state.detailed_improvement_plan = None

    if page == "Resume Analysis":
        st.title("Smart Application Tracking System")
        st.text("Improve Your Resume ATS")
        
        jd = st.text_area("Paste the Job Description")
        uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

        submit = st.button("Submit")

        if submit:
            if uploaded_file is not None:
                text = input_pdf_text(uploaded_file)
                formatted_prompt = input_prompt.format(text=text, jd=jd)
                response = get_cohere_response(formatted_prompt)
                
                try:
                    response = response.replace('\n', ' ').strip()
                    if response.startswith("```json"):
                        response = response[7:]
                    if response.endswith("```"):
                        response = response[:-3]
                    
                    # Clean up the response further
                    response = response.strip()
                    
                    # Try to clean up the response if it's not valid JSON
                    try:
                        response_dict = json.loads(response)
                    except json.JSONDecodeError as e:
                        # If JSON parsing fails, try to extract JSON from the response
                        import re
                        # Try multiple patterns to extract JSON
                        json_patterns = [
                            r'\{.*\}',
                            r'\{[^}]*"JD Match"[^}]*\}',
                            r'\{[^}]*"MissingKeywords"[^}]*\}',
                            r'\{[^}]*"Profile Summary"[^}]*\}'
                        ]
                        
                        response_dict = None
                        for pattern in json_patterns:
                            json_match = re.search(pattern, response, re.DOTALL)
                            if json_match:
                                try:
                                    response_dict = json.loads(json_match.group())
                                    break
                                except json.JSONDecodeError:
                                    continue
                        
                        if response_dict is None:
                            st.error("Unable to parse response as JSON. Please try again.")
                            st.text("Raw response for debugging:")
                            st.code(response)
                            st.text(f"JSON Error: {str(e)}")
                            st.stop()
                    
                    # Handle Profile Summary if it's an array instead of string
                    if 'Profile Summary' in response_dict and isinstance(response_dict['Profile Summary'], list):
                        response_dict['Profile Summary'] = ' '.join(response_dict['Profile Summary'])
                    
                    # Validate the response structure
                    required_keys = ['JD Match', 'MissingKeywords', 'Profile Summary']
                    if not all(key in response_dict for key in required_keys):
                        st.error("Response missing required fields. Please try again.")
                        st.text("Raw response for debugging:")
                        st.code(response)
                        st.stop()
                    
                    # Store results in session state
                    st.session_state.analysis_results = response_dict
                    
                    # Redirect to results page
                    st.success("Analysis completed! Navigate to 'Analysis Results' to view your results.")
                    
                except Exception as e:
                    st.error(f"Error processing the response. Please try again. Error: {str(e)}")
                    st.text("Raw response for debugging:")
                    st.code(response)
            else:
                st.error("Please upload a PDF resume first.")

    elif page == "Analysis Results":
        st.title("📊 Resume Analysis Results")
        
        if st.session_state.analysis_results is None:
            st.warning("⚠️ Please analyze your resume first in the Resume Analysis page.")
            st.markdown("Go to the 'Resume Analysis' page to upload your resume and get started.")
        else:
            response_dict = st.session_state.analysis_results
            
            # Add ATS Score Meter
            st.subheader("📈 ATS Score Meter")
            match_percentage = response_dict['JD Match']
            # Handle both string and integer percentage values
            if isinstance(match_percentage, str):
                match_percentage = match_percentage.rstrip('%')
            else:
                match_percentage = str(match_percentage)
            match_value = int(match_percentage) if match_percentage.isdigit() else 0
            
            col1, col2, col3 = st.columns([1, 3, 1])
            with col2:
                progress_bar = st.progress(0)
                progress_bar.progress(match_value / 100)
                
                if match_value >= 70:
                    st.success(f"Strong Match 💪 ({match_value}%)")
                    st.markdown("*Your resume is well-aligned with the job requirements!*")
                elif match_value >= 40:
                    st.warning(f"Moderate Match 🤔 ({match_value}%)")
                    st.markdown("*Consider addressing the missing keywords to improve your match.*")
                else:
                    st.error(f"Low Match 😟 ({match_value}%)")
                    st.markdown("*Significant improvements needed to match job requirements.*")
            
            st.markdown("---")
            
            if match_value >= 70:
                st.success(f"🎯 JD Match: {response_dict['JD Match']}")
            elif match_value >= 40:
                st.warning(f"🎯 JD Match: {response_dict['JD Match']}")
            else:
                st.error(f"🎯 JD Match: {response_dict['JD Match']}")
            
            st.subheader("🔍 Missing Keywords")
            for keyword in response_dict['MissingKeywords']:
                st.markdown(f"- {keyword}")
            
            st.subheader("📋 Profile Summary")
            st.info(response_dict['Profile Summary'])
            
            # Button to go to improvement tips
            st.markdown("---")
            if st.button("📝 Resume Improvement Tips", type="primary"):
                st.success("Navigate to 'Resume Improvement Tips' to get personalized suggestions!")

    elif page == "Resume Improvement Tips":
        st.title("Resume Improvement Tips")
        
        if st.session_state.analysis_results is None:
            st.warning("⚠️ Please analyze your resume first in the Resume Analysis page to get personalized improvement tips.")
            st.markdown("""
            ### General Resume Tips:
            1. **Use ATS-friendly formatting**
               - Stick to standard fonts (Arial, Calibri, Times New Roman)
               - Use common section headings
               - Avoid tables and graphics
            
            2. **Keywords are crucial**
               - Match keywords from the job description
               - Use industry-standard terminology
               
            3. **Quantify achievements**
               - Use numbers and percentages
               - Show impact with metrics
               
            4. **Be concise but comprehensive**
               - Keep to 1-2 pages
               - Focus on relevant experience
               
            5. **Proofread thoroughly**
               - Check for spelling and grammar
               - Ensure consistent formatting
            """)
        else:
            st.header("🎯 Personalized Improvement Suggestions")
            
            # Get the analysis results
            results = st.session_state.analysis_results
            match_percentage = results['JD Match']
            # Handle both string and integer percentage values
            if isinstance(match_percentage, str):
                match_percentage = match_percentage.rstrip('%')
            else:
                match_percentage = str(match_percentage)
            match_value = int(match_percentage) if match_percentage.isdigit() else 0
            
            # Display current score
            st.metric("Current ATS Score", f"{match_value}%")
            
            # Keywords section
            st.subheader("📝 Keywords to Include")
            st.write("Add these missing keywords to your resume in relevant contexts:")
            for keyword in results['MissingKeywords']:
                st.markdown(f"- `{keyword}`")
                
            # Generate improvement prompt
            improvement_prompt = f"""
            Based on the following analysis:
            - Current Match: {results['JD Match']}
            - Missing Keywords: {', '.join(results['MissingKeywords'])}
            - Current Profile: {results['Profile Summary']}

            Provide specific suggestions for improving the resume, including:
            1. How to incorporate the missing keywords naturally
            2. Sample achievement statements
            3. Skills section improvements
            4. Overall structure suggestions

            Format the response in clear sections with bullet points.
            """
            
            if st.button("Generate Detailed Improvement Plan", type="primary"):
                with st.spinner("Generating improvement suggestions..."):
                    suggestions = get_cohere_response(improvement_prompt)
                    st.session_state.detailed_improvement_plan = suggestions
                    st.success("Detailed improvement plan generated! Navigate to 'Detailed Improvement Plan' to view it.")
                    
            st.markdown("---")
            
            # General tips based on score
            st.subheader("💡 Quick Tips")
            if match_value < 40:
                st.error("Priority Actions:")
                st.markdown("""
                - Completely restructure your resume to align with the job requirements
                - Add specific examples of relevant projects/experience
                - Focus on incorporating the missing keywords in your experience section
                """)
            elif match_value < 70:
                st.warning("Suggested Improvements:")
                st.markdown("""
                - Enhance your skills section with the missing keywords
                - Quantify your achievements more clearly
                - Reorganize sections to highlight relevant experience
                """)
            else:
                st.success("Fine-tuning Suggestions:")
                st.markdown("""
                - Add more specific industry terminology
                - Enhance achievement metrics
                - Consider adding relevant certifications
                """)

    elif page == "Detailed Improvement Plan":
        st.title("📈 Detailed Improvement Plan")
        
        if st.session_state.detailed_improvement_plan is None:
            st.warning("⚠️ Please generate a detailed improvement plan first in the Resume Improvement Tips page.")
            st.markdown("Go to 'Resume Improvement Tips' and click 'Generate Detailed Improvement Plan' to get started.")
        else:
            st.markdown("### 📈 Detailed Improvement Plan")
            st.markdown(st.session_state.detailed_improvement_plan)
            
            st.markdown("---")
            st.info("💡 Use these suggestions to improve your resume and increase your ATS score!")

    elif page == "User Profile":
        auth_manager.show_user_profile()

def main():
    """Main application function"""
    # Set page config
    st.set_page_config(
        page_title="Smart Resume ATS",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Check authentication status
    if not auth_manager.is_authenticated():
        show_authentication_page()
    else:
        show_main_application()

if __name__ == "__main__":
    main()
