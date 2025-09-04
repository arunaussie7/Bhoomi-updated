import streamlit as st
import json
import re
from datetime import datetime
import PyPDF2 as pdf
from io import BytesIO
import base64

class AdvancedResumeAnalyzer:
    def __init__(self, cohere_client):
        self.co = cohere_client
    
    def get_cohere_response(self, input_text):
        """Get response from Cohere AI"""
        response = self.co.generate(
            model='command',
            prompt=input_text,
            max_tokens=2000,
            temperature=0.7,
            k=0,
            stop_sequences=[],
            return_likelihoods='NONE'
        )
        return response.generations[0].text.strip()
    
    def extract_resume_sections(self, resume_text):
        """Extract different sections from resume text"""
        sections = {
            'contact_info': '',
            'summary': '',
            'experience': '',
            'education': '',
            'skills': '',
            'certifications': '',
            'projects': ''
        }
        
        # Extract contact information
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        phone_pattern = r'(\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})'
        
        emails = re.findall(email_pattern, resume_text)
        phones = re.findall(phone_pattern, resume_text)
        
        if emails:
            sections['contact_info'] += f"Email: {emails[0]}\n"
        if phones:
            sections['contact_info'] += f"Phone: {''.join(phones[0])}\n"
        
        # Extract sections using common headers
        section_patterns = {
            'summary': r'(?i)(summary|profile|objective|about)\s*:?\s*(.*?)(?=\n\s*[A-Z][A-Z\s]+:|\n\s*[A-Z][a-z]+\s*[A-Z][a-z]+|\Z)',
            'experience': r'(?i)(experience|work\s*history|employment|professional\s*experience)\s*:?\s*(.*?)(?=\n\s*[A-Z][A-Z\s]+:|\n\s*[A-Z][a-z]+\s*[A-Z][a-z]+|\Z)',
            'education': r'(?i)(education|academic|qualifications)\s*:?\s*(.*?)(?=\n\s*[A-Z][A-Z\s]+:|\n\s*[A-Z][a-z]+\s*[A-Z][a-z]+|\Z)',
            'skills': r'(?i)(skills|technical\s*skills|competencies)\s*:?\s*(.*?)(?=\n\s*[A-Z][A-Z\s]+:|\n\s*[A-Z][a-z]+\s*[A-Z][a-z]+|\Z)',
            'certifications': r'(?i)(certifications|certificates|licenses)\s*:?\s*(.*?)(?=\n\s*[A-Z][A-Z\s]+:|\n\s*[A-Z][a-z]+\s*[A-Z][a-z]+|\Z)',
            'projects': r'(?i)(projects|portfolio|key\s*projects)\s*:?\s*(.*?)(?=\n\s*[A-Z][A-Z\s]+:|\n\s*[A-Z][a-z]+\s*[A-Z][a-z]+|\Z)'
        }
        
        for section, pattern in section_patterns.items():
            match = re.search(pattern, resume_text, re.DOTALL)
            if match:
                sections[section] = match.group(2).strip()
        
        return sections
    
    def optimize_resume_section(self, section_content, job_description, section_type):
        """Optimize a specific resume section based on job description"""
        
        optimization_prompts = {
            'summary': f"""
            Optimize this professional summary for the given job description. Make it more compelling and ATS-friendly.
            
            Current Summary: {section_content}
            Job Description: {job_description}
            
            Requirements:
            1. Keep it 3-4 sentences maximum
            2. Include relevant keywords from the job description
            3. Highlight key achievements and skills
            4. Make it action-oriented and results-focused
            5. Ensure it's ATS-friendly (no special characters, clear formatting)
            
            Return only the optimized summary:
            """,
            
            'experience': f"""
            Optimize this work experience section for the given job description. Make it more impactful and ATS-friendly.
            
            Current Experience: {section_content}
            Job Description: {job_description}
            
            Requirements:
            1. Use action verbs to start each bullet point
            2. Include quantifiable achievements (numbers, percentages, metrics)
            3. Incorporate relevant keywords from the job description
            4. Focus on results and impact
            5. Keep each bullet point concise (1-2 lines)
            6. Ensure ATS-friendly formatting
            
            Return the optimized experience section:
            """,
            
            'skills': f"""
            Optimize this skills section for the given job description. Make it more relevant and ATS-friendly.
            
            Current Skills: {section_content}
            Job Description: {job_description}
            
            Requirements:
            1. Prioritize skills mentioned in the job description
            2. Group related skills together
            3. Include both technical and soft skills
            4. Use industry-standard terminology
            5. Keep it concise and scannable
            6. Ensure ATS-friendly formatting
            
            Return the optimized skills section:
            """,
            
            'education': f"""
            Optimize this education section for the given job description. Make it more relevant and ATS-friendly.
            
            Current Education: {section_content}
            Job Description: {job_description}
            
            Requirements:
            1. Highlight relevant coursework or specializations
            2. Include academic achievements if relevant
            3. Use standard formatting
            4. Focus on education that matches job requirements
            5. Ensure ATS-friendly formatting
            
            Return the optimized education section:
            """
        }
        
        if section_type in optimization_prompts:
            return self.get_cohere_response(optimization_prompts[section_type])
        return section_content
    
    def generate_ats_optimized_resume(self, resume_text, job_description, analysis_results):
        """Generate a complete ATS-optimized resume"""
        
        # Extract resume sections
        sections = self.extract_resume_sections(resume_text)
        
        # Get missing keywords from analysis
        missing_keywords = analysis_results.get('MissingKeywords', [])
        match_percentage = analysis_results.get('JD Match', '0%')
        
        # Create optimization prompt
        optimization_prompt = f"""
        Create a complete ATS-optimized resume based on the following information:
        
        Original Resume Sections:
        {json.dumps(sections, indent=2)}
        
        Job Description: {job_description}
        
        Current ATS Score: {match_percentage}
        Missing Keywords to Include: {', '.join(missing_keywords)}
        
        Requirements:
        1. Create a professional, ATS-friendly resume format
        2. Incorporate all missing keywords naturally
        3. Optimize each section for maximum ATS compatibility
        4. Use action verbs and quantifiable achievements
        5. Ensure proper formatting and structure
        6. Include all relevant information from the original resume
        7. Make it compelling for both ATS and human readers
        
        Return the complete optimized resume in the following format:
        
        [CONTACT INFORMATION]
        [Name, Email, Phone, LinkedIn, Location]
        
        [PROFESSIONAL SUMMARY]
        [Optimized 3-4 sentence summary]
        
        [TECHNICAL SKILLS]
        [Relevant skills with keywords]
        
        [PROFESSIONAL EXPERIENCE]
        [Optimized experience with achievements]
        
        [EDUCATION]
        [Relevant education information]
        
        [CERTIFICATIONS] (if applicable)
        [Relevant certifications]
        
        [PROJECTS] (if applicable)
        [Key projects with results]
        """
        
        optimized_resume = self.get_cohere_response(optimization_prompt)
        return optimized_resume
    
    def generate_resume_improvements(self, resume_text, job_description, analysis_results):
        """Generate specific improvement suggestions"""
        
        missing_keywords = analysis_results.get('MissingKeywords', [])
        match_percentage = analysis_results.get('JD Match', '0%')
        
        improvement_prompt = f"""
        Based on the resume analysis, provide specific improvement recommendations:
        
        Current ATS Score: {match_percentage}
        Missing Keywords: {', '.join(missing_keywords)}
        Job Description: {job_description}
        
        Provide detailed recommendations in the following categories:
        
        1. KEYWORD OPTIMIZATION
        2. CONTENT IMPROVEMENTS
        3. FORMATTING ENHANCEMENTS
        4. ACHIEVEMENT QUANTIFICATION
        5. SKILLS ALIGNMENT
        6. EXPERIENCE OPTIMIZATION
        
        For each category, provide:
        - Specific actionable recommendations
        - Examples of improvements
        - Expected impact on ATS score
        
        Format as a comprehensive improvement guide.
        """
        
        improvements = self.get_cohere_response(improvement_prompt)
        return improvements
    
    def create_resume_template(self, job_description, user_profile):
        """Create a custom resume template based on job requirements"""
        
        template_prompt = f"""
        Create a custom ATS-friendly resume template for the following job:
        
        Job Description: {job_description}
        User Profile: {user_profile}
        
        Create a professional resume template with:
        1. Optimal section order for this job type
        2. Recommended section headers
        3. Formatting guidelines
        4. Keyword placement strategies
        5. ATS optimization tips
        
        Return a structured template with placeholders and instructions.
        """
        
        template = self.get_cohere_response(template_prompt)
        return template

def show_advanced_analysis_page():
    """Display the Advanced Analysis page"""
    
    st.title("🚀 Advanced Resume Analysis & Optimization")
    st.markdown("Transform your resume into an ATS-optimized, job-winning document!")
    
    # Check if user has analysis results
    if 'analysis_results' not in st.session_state or st.session_state.analysis_results is None:
        st.warning("⚠️ Please complete a resume analysis first to use Advanced Analysis features.")
        st.markdown("Go to 'Resume Analysis' to upload your resume and get started.")
        return
    
    # Get analysis results and resume data
    analysis_results = st.session_state.analysis_results
    job_description = st.session_state.get('job_description', '')
    resume_text = st.session_state.get('resume_text', '')
    
    if not resume_text:
        st.error("Resume text not found. Please re-upload your resume.")
        return
    
    # Initialize advanced analyzer
    from dotenv import load_dotenv
    import os
    import cohere
    
    load_dotenv()
    co = cohere.Client(os.getenv("COHERE_API_KEY"))
    analyzer = AdvancedResumeAnalyzer(co)
    
    # Create tabs for different features
    tab1, tab2, tab3, tab4 = st.tabs([
        "🎯 Resume Optimization", 
        "📊 Improvement Guide", 
        "📝 Resume Template", 
        "💡 Smart Suggestions"
    ])
    
    with tab1:
        st.subheader("🎯 Generate ATS-Optimized Resume")
        st.markdown("Transform your resume into a job-winning document optimized for ATS systems.")
        
        if st.button("🚀 Generate Optimized Resume", type="primary"):
            with st.spinner("Analyzing and optimizing your resume..."):
                try:
                    optimized_resume = analyzer.generate_ats_optimized_resume(
                        resume_text, job_description, analysis_results
                    )
                    
                    st.session_state.optimized_resume = optimized_resume
                    st.success("✅ Optimized resume generated successfully!")
                    
                    # Display the optimized resume
                    st.subheader("📄 Your ATS-Optimized Resume")
                    st.text_area("Optimized Resume", optimized_resume, height=600)
                    
                    # Download button
                    st.download_button(
                        label="📥 Download Optimized Resume",
                        data=optimized_resume,
                        file_name=f"optimized_resume_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain"
                    )
                    
                except Exception as e:
                    st.error(f"Error generating optimized resume: {str(e)}")
    
    with tab2:
        st.subheader("📊 Detailed Improvement Guide")
        st.markdown("Get specific recommendations to improve your resume's ATS compatibility.")
        
        if st.button("📈 Generate Improvement Guide", type="primary"):
            with st.spinner("Generating improvement recommendations..."):
                try:
                    improvements = analyzer.generate_resume_improvements(
                        resume_text, job_description, analysis_results
                    )
                    
                    st.session_state.improvement_guide = improvements
                    st.success("✅ Improvement guide generated successfully!")
                    
                    # Display improvements
                    st.markdown("### 📋 Your Personalized Improvement Guide")
                    st.markdown(improvements)
                    
                except Exception as e:
                    st.error(f"Error generating improvement guide: {str(e)}")
    
    with tab3:
        st.subheader("📝 Resume Templates & Custom Generation")
        st.markdown("Choose from professional templates or generate a custom one based on your job.")
        
        # Template selection
        from resume_templates import ResumeTemplates
        template_manager = ResumeTemplates()
        
        # Show template selector
        template_content, template_key = template_manager.show_template_selector()
        
        st.markdown("---")
        
        # Custom template generation
        st.subheader("🎯 Generate Custom Template")
        st.markdown("Get a personalized resume template based on your target job and profile.")
        
        if st.button("📋 Generate Custom Template", type="primary"):
            with st.spinner("Creating custom resume template..."):
                try:
                    user_profile = analysis_results.get('Profile Summary', '')
                    custom_template = analyzer.create_resume_template(job_description, user_profile)
                    
                    st.session_state.resume_template = custom_template
                    st.success("✅ Custom template generated successfully!")
                    
                    # Display custom template
                    st.markdown("### 📄 Your Custom Resume Template")
                    st.text_area("Custom Resume Template", custom_template, height=600)
                    
                    # Download custom template
                    st.download_button(
                        label="📥 Download Custom Template",
                        data=custom_template,
                        file_name=f"custom_resume_template_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain"
                    )
                    
                except Exception as e:
                    st.error(f"Error generating custom template: {str(e)}")
    
    with tab4:
        st.subheader("💡 Smart Suggestions")
        st.markdown("Get AI-powered suggestions for resume enhancement.")
        
        # Display current analysis
        st.markdown("### 📊 Current Analysis Results")
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("ATS Score", analysis_results.get('JD Match', '0%'))
        
        with col2:
            missing_count = len(analysis_results.get('MissingKeywords', []))
            st.metric("Missing Keywords", missing_count)
        
        # Show missing keywords
        if analysis_results.get('MissingKeywords'):
            st.markdown("### 🔍 Missing Keywords to Include")
            for keyword in analysis_results['MissingKeywords']:
                st.markdown(f"- `{keyword}`")
        
        # Smart suggestions based on analysis
        st.markdown("### 💡 Smart Suggestions")
        
        match_percentage = analysis_results.get('JD Match', '0%')
        if isinstance(match_percentage, str):
            match_percentage = match_percentage.rstrip('%')
        match_value = int(match_percentage) if match_percentage.isdigit() else 0
        
        if match_value < 40:
            st.error("🚨 Priority Actions Needed:")
            st.markdown("""
            - **Complete Resume Overhaul**: Your resume needs significant restructuring
            - **Keyword Integration**: Add missing keywords throughout your resume
            - **Experience Alignment**: Restructure experience to match job requirements
            - **Skills Enhancement**: Add relevant technical and soft skills
            """)
        elif match_value < 70:
            st.warning("⚠️ Moderate Improvements Needed:")
            st.markdown("""
            - **Keyword Optimization**: Incorporate missing keywords naturally
            - **Achievement Quantification**: Add numbers and metrics to your experience
            - **Skills Section**: Enhance your skills section with relevant keywords
            - **Summary Optimization**: Rewrite your professional summary
            """)
        else:
            st.success("✅ Fine-tuning Opportunities:")
            st.markdown("""
            - **Keyword Density**: Optimize keyword placement and frequency
            - **Achievement Enhancement**: Add more specific metrics and results
            - **Industry Terminology**: Use more industry-specific language
            - **Certification Addition**: Consider adding relevant certifications
            """)
        
        # Quick actions
        st.markdown("### ⚡ Quick Actions")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔄 Re-analyze Resume"):
                st.info("Go to 'Resume Analysis' to re-upload and analyze your resume")
        
        with col2:
            if st.button("📊 View Full Results"):
                st.info("Go to 'Analysis Results' to see detailed analysis")
        
        with col3:
            if st.button("💡 Get Improvement Tips"):
                st.info("Go to 'Resume Improvement Tips' for detailed suggestions")
