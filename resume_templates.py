import streamlit as st
from datetime import datetime

class ResumeTemplates:
    def __init__(self):
        self.templates = {
            'professional': self.get_professional_template(),
            'technical': self.get_technical_template(),
            'executive': self.get_executive_template(),
            'entry_level': self.get_entry_level_template(),
            'creative': self.get_creative_template()
        }
    
    def get_professional_template(self):
        """Professional resume template"""
        return """
[YOUR NAME]
[Email Address] | [Phone Number] | [LinkedIn Profile] | [Location]

PROFESSIONAL SUMMARY
• [3-4 sentences highlighting your key qualifications, experience, and career objectives]
• [Include relevant keywords from the job description]
• [Mention years of experience and key achievements]

TECHNICAL SKILLS
• [Programming Languages]: [List relevant languages]
• [Software/Tools]: [List relevant software and tools]
• [Frameworks]: [List relevant frameworks]
• [Databases]: [List relevant databases]
• [Other Skills]: [List other relevant technical skills]

PROFESSIONAL EXPERIENCE

[Job Title] | [Company Name] | [Location] | [Start Date - End Date]
• [Action verb] [specific achievement with quantifiable results]
• [Action verb] [specific achievement with quantifiable results]
• [Action verb] [specific achievement with quantifiable results]

[Job Title] | [Company Name] | [Location] | [Start Date - End Date]
• [Action verb] [specific achievement with quantifiable results]
• [Action verb] [specific achievement with quantifiable results]
• [Action verb] [specific achievement with quantifiable results]

EDUCATION
[Degree] in [Field of Study] | [University Name] | [Location] | [Graduation Date]
• [Relevant coursework, honors, or achievements]

CERTIFICATIONS
• [Certification Name] | [Issuing Organization] | [Date]
• [Certification Name] | [Issuing Organization] | [Date]

PROJECTS (if applicable)
[Project Name] | [Technologies Used] | [Date]
• [Brief description of the project and your role]
• [Key achievements and results]
        """
    
    def get_technical_template(self):
        """Technical resume template optimized for tech roles"""
        return """
[YOUR NAME]
[Email] | [Phone] | [GitHub Profile] | [LinkedIn] | [Location]

TECHNICAL SUMMARY
• [X+ years of experience in [relevant technologies]]
• [Expertise in [key technical areas]]
• [Notable achievements or projects]
• [Relevant certifications or specializations]

TECHNICAL SKILLS
Programming Languages: [List languages with proficiency levels]
Frameworks & Libraries: [List relevant frameworks]
Databases: [List databases and proficiency]
Cloud Platforms: [List cloud platforms and services]
Tools & Technologies: [List development tools, IDEs, etc.]
Methodologies: [List relevant methodologies like Agile, DevOps, etc.]

PROFESSIONAL EXPERIENCE

[Senior/Lead] [Job Title] | [Company] | [Location] | [Dates]
• [Developed/Implemented/Architected] [specific technical solution] resulting in [quantifiable impact]
• [Led/Mentored] team of [X] developers in [specific project or initiative]
• [Optimized/Improved] [system/process] by [X]% resulting in [specific benefit]
• [Technologies used]: [List key technologies]

[Job Title] | [Company] | [Location] | [Dates]
• [Built/Designed/Created] [specific technical solution] using [technologies]
• [Collaborated with] [teams/departments] to [achieve specific goal]
• [Resolved/Improved] [technical challenge] resulting in [quantifiable outcome]
• [Technologies used]: [List key technologies]

EDUCATION
[Degree] in [Computer Science/Engineering/Related Field] | [University] | [Date]
• [Relevant coursework, projects, or achievements]

CERTIFICATIONS
• [AWS/Azure/GCP Certification] | [Issuing Organization] | [Date]
• [Technology-specific Certification] | [Issuing Organization] | [Date]

KEY PROJECTS
[Project Name] | [Technologies] | [Date]
• [Brief description of the technical challenge and solution]
• [Your specific role and contributions]
• [Technologies used and results achieved]

[Project Name] | [Technologies] | [Date]
• [Brief description of the technical challenge and solution]
• [Your specific role and contributions]
• [Technologies used and results achieved]
        """
    
    def get_executive_template(self):
        """Executive resume template for senior leadership roles"""
        return """
[YOUR NAME]
[Email] | [Phone] | [LinkedIn Profile] | [Location]

EXECUTIVE SUMMARY
• [X+ years of progressive leadership experience in [industry/domain]]
• [Track record of driving growth, transformation, and operational excellence]
• [Key leadership achievements with quantifiable business impact]
• [Vision and strategic thinking capabilities]

CORE COMPETENCIES
Strategic Planning & Execution | Team Leadership & Development | Financial Management
Business Development | Operations Management | Change Management
[Industry-specific competencies]

PROFESSIONAL EXPERIENCE

[VP/Director/Chief] [Job Title] | [Company] | [Location] | [Dates]
• [Led/Transformed/Expanded] [business unit/function] resulting in [quantifiable business impact]
• [Managed/Developed] team of [X] professionals across [departments/regions]
• [Implemented/Launched] [strategic initiative] that [specific business outcome]
• [Achieved/Exceeded] [financial/business targets] by [X]% through [specific strategies]

[Senior] [Job Title] | [Company] | [Location] | [Dates]
• [Directed/Oversaw] [major business function] with [X] budget responsibility
• [Built/Developed] [strategic partnerships/alliances] resulting in [business impact]
• [Led/Executed] [major project/initiative] that [specific outcome]
• [Improved/Enhanced] [business process/metric] by [X]% through [specific actions]

[Job Title] | [Company] | [Location] | [Dates]
• [Managed/Led] [team/function] in [specific business area]
• [Developed/Implemented] [strategic plan/initiative] resulting in [outcome]
• [Collaborated with] [stakeholders] to [achieve specific goal]
• [Delivered/Exceeded] [business targets] through [specific strategies]

EDUCATION
[Degree] in [Field] | [University] | [Date]
• [Relevant coursework, honors, or achievements]

PROFESSIONAL DEVELOPMENT
• [Executive Education Program] | [Institution] | [Date]
• [Leadership Certification] | [Organization] | [Date]
• [Industry-specific Training] | [Provider] | [Date]

BOARD MEMBERSHIPS & AFFILIATIONS
• [Board Position] | [Organization] | [Dates]
• [Professional Association] | [Role] | [Dates]
        """
    
    def get_entry_level_template(self):
        """Entry-level resume template for recent graduates"""
        return """
[YOUR NAME]
[Email] | [Phone] | [LinkedIn Profile] | [Location]

PROFESSIONAL SUMMARY
• [Recent graduate with degree in [field] and passion for [industry/role]]
• [Relevant coursework, projects, or internships in [specific area]]
• [Key skills and competencies relevant to target role]
• [Motivated and eager to contribute to [specific type of organization]]

EDUCATION
[Degree] in [Field of Study] | [University Name] | [Location] | [Graduation Date]
• GPA: [X.XX/4.0] (if 3.5 or higher)
• Relevant Coursework: [List relevant courses]
• [Honors, Dean's List, or other academic achievements]

RELEVANT EXPERIENCE

[Internship/Part-time Job Title] | [Company] | [Location] | [Dates]
• [Action verb] [specific task or project] resulting in [outcome]
• [Collaborated with] [team members] to [achieve specific goal]
• [Gained experience in] [relevant skills or technologies]
• [Contributed to] [specific project or initiative]

[Volunteer/Project Role] | [Organization] | [Location] | [Dates]
• [Action verb] [specific responsibility or achievement]
• [Developed/Improved] [specific skill or process]
• [Worked with] [team/stakeholders] to [achieve goal]

TECHNICAL SKILLS
• [Programming Languages]: [List languages with proficiency levels]
• [Software/Tools]: [List relevant software and tools]
• [Frameworks]: [List relevant frameworks]
• [Other Skills]: [List other relevant technical skills]

PROJECTS
[Project Name] | [Technologies Used] | [Date]
• [Brief description of the project and your role]
• [Technologies used and key features implemented]
• [Results achieved or lessons learned]

[Project Name] | [Technologies Used] | [Date]
• [Brief description of the project and your role]
• [Technologies used and key features implemented]
• [Results achieved or lessons learned]

CERTIFICATIONS & TRAINING
• [Relevant Certification] | [Issuing Organization] | [Date]
• [Online Course/Training] | [Platform] | [Date]

ACTIVITIES & LEADERSHIP
• [Leadership Role] | [Organization] | [Dates]
• [Volunteer Work] | [Organization] | [Dates]
• [Relevant Activities] | [Organization] | [Dates]
        """
    
    def get_creative_template(self):
        """Creative resume template for design and creative roles"""
        return """
[YOUR NAME]
[Email] | [Phone] | [Portfolio Website] | [LinkedIn] | [Location]

CREATIVE PROFESSIONAL
• [X+ years of experience in [creative field/industry]]
• [Specialized expertise in [specific creative areas]]
• [Notable projects, clients, or achievements]
• [Creative vision and innovative approach to problem-solving]

CREATIVE SKILLS
Design Software: [List design tools with proficiency levels]
Technical Skills: [List relevant technical skills]
Creative Disciplines: [List areas of expertise]
Project Management: [List relevant project management skills]
Collaboration Tools: [List relevant collaboration platforms]

PROFESSIONAL EXPERIENCE

[Senior/Creative] [Job Title] | [Company] | [Location] | [Dates]
• [Designed/Created/Developed] [specific creative solution] for [client/project]
• [Led/Collaborated on] [creative project] resulting in [specific outcome]
• [Managed/Mentored] [team size] creative professionals
• [Technologies/Tools used]: [List key creative tools and technologies]

[Creative] [Job Title] | [Company] | [Location] | [Dates]
• [Conceptualized/Executed] [creative project] that [specific achievement]
• [Collaborated with] [teams/clients] to [achieve creative goal]
• [Innovated/Improved] [creative process/solution] resulting in [outcome]
• [Portfolio pieces]: [Brief description of notable work]

EDUCATION
[Degree] in [Design/Creative Field] | [University] | [Date]
• [Relevant coursework, projects, or achievements]
• [Study abroad, special programs, or honors]

CERTIFICATIONS & TRAINING
• [Design Software Certification] | [Issuing Organization] | [Date]
• [Creative Workshop/Training] | [Provider] | [Date]
• [Industry-specific Training] | [Organization] | [Date]

NOTABLE PROJECTS
[Project Name] | [Client/Company] | [Date]
• [Brief description of the creative challenge and solution]
• [Your specific role and creative contributions]
• [Technologies used and results achieved]
• [Link to portfolio piece if available]

[Project Name] | [Client/Company] | [Date]
• [Brief description of the creative challenge and solution]
• [Your specific role and creative contributions]
• [Technologies used and results achieved]
• [Link to portfolio piece if available]

AWARDS & RECOGNITION
• [Award Name] | [Organization] | [Date]
• [Recognition/Publication] | [Source] | [Date]
        """
    
    def get_template_by_industry(self, industry):
        """Get template based on industry"""
        industry_templates = {
            'technology': 'technical',
            'software': 'technical',
            'engineering': 'technical',
            'healthcare': 'professional',
            'finance': 'professional',
            'marketing': 'creative',
            'design': 'creative',
            'education': 'professional',
            'consulting': 'executive',
            'management': 'executive',
            'entry_level': 'entry_level',
            'internship': 'entry_level'
        }
        
        template_type = industry_templates.get(industry.lower(), 'professional')
        return self.templates[template_type]
    
    def show_template_selector(self):
        """Display template selection interface"""
        st.subheader("📝 Choose Your Resume Template")
        
        # Template selection
        template_options = {
            'Professional': 'professional',
            'Technical (IT/Software)': 'technical',
            'Executive (Leadership)': 'executive',
            'Entry Level (Recent Graduate)': 'entry_level',
            'Creative (Design/Marketing)': 'creative'
        }
        
        selected_template = st.selectbox(
            "Select Template Type:",
            options=list(template_options.keys()),
            help="Choose the template that best fits your career level and industry"
        )
        
        template_key = template_options[selected_template]
        template_content = self.templates[template_key]
        
        # Display template
        st.subheader(f"📄 {selected_template} Template")
        st.text_area(
            "Resume Template",
            template_content,
            height=600,
            help="Copy this template and fill in your information"
        )
        
        # Download template
        st.download_button(
            label="📥 Download Template",
            data=template_content,
            file_name=f"{template_key}_resume_template_{datetime.now().strftime('%Y%m%d')}.txt",
            mime="text/plain"
        )
        
        # Template tips
        st.markdown("### 💡 Template Tips")
        
        if template_key == 'professional':
            st.markdown("""
            **Professional Template Tips:**
            - Use action verbs to start each bullet point
            - Include quantifiable achievements
            - Keep formatting consistent and clean
            - Use standard section headers
            - Ensure ATS-friendly formatting
            """)
        elif template_key == 'technical':
            st.markdown("""
            **Technical Template Tips:**
            - List technologies with proficiency levels
            - Include specific project details
            - Highlight technical achievements
            - Use industry-standard terminology
            - Include GitHub/portfolio links
            """)
        elif template_key == 'executive':
            st.markdown("""
            **Executive Template Tips:**
            - Focus on leadership and strategic achievements
            - Include quantifiable business impact
            - Highlight team management experience
            - Emphasize financial and operational results
            - Include board memberships and affiliations
            """)
        elif template_key == 'entry_level':
            st.markdown("""
            **Entry Level Template Tips:**
            - Emphasize relevant coursework and projects
            - Include internships and volunteer work
            - Highlight transferable skills
            - Show enthusiasm and motivation
            - Include academic achievements if strong
            """)
        elif template_key == 'creative':
            st.markdown("""
            **Creative Template Tips:**
            - Include portfolio links
            - Highlight creative achievements
            - Show range of creative skills
            - Include client work and projects
            - Emphasize innovation and creativity
            """)
        
        return template_content, template_key
