import streamlit as st
from streamlit_form import resume_form

# Must be the first Streamlit command
st.set_page_config(page_title='Resume', page_icon='📄', layout='centered')

def main():
    st.title("Resume Builder")
    
    # Display the form first
    resume_form()
    
    if 'resume_data' in st.session_state:
        data = st.session_state['resume_data']
        
        # Header Section
        st.markdown(f"""
            <h1 style='color: #D32F2F;'>{data['name']}</h1>
            <h3>{data['title']}</h3>
            <p><strong>Email:</strong> {data['email']}</p>
            <p><strong>Phone:</strong> {data['phone']}</p>
            <p><strong>Location:</strong> {data['location']}</p>
            <hr style='border: 2px solid red;'>
        """, unsafe_allow_html=True)
        
        # Professional Summary
        st.subheader("Professional Summary")
        st.write(data['summary'])
        
        # Experience Section
        st.subheader("Experience")
        st.write(f"### {data['company']}")
        st.write(f"#### {data['position']}")
        st.write(data['experience_details'])
        
        # Skills Section
        st.subheader("Skills")
        skills = [skill.strip() for skill in data['skills'].split(',') if skill.strip()]
        for i, skill in enumerate(skills):
            # Create a more visually appealing alternating pattern
            progress_value = 0.6 + (i % 2) * 0.2  # Alternates between 60% and 80%
            st.progress(progress_value)
            st.write(f"**{skill}**")
        
        # Certifications
        st.subheader("Certifications")
        st.write(data['certifications'])
        
        # Education
        st.subheader("Education")
        st.write(data['education'])
        
        # Languages
        st.subheader("Languages")
        languages = [lang.strip() for lang in data['languages'].split(',') if lang.strip()]
        for lang in languages:
            st.write(f"- {lang}")
    
if __name__ == "__main__":
    main()
