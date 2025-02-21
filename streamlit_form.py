import streamlit as st
from fpdf import FPDF
import base64

def generate_pdf(data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, data.get('name', 'N/A'), ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, data.get('title', 'N/A'), ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(0, 10, "Contact Information", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Email: {data.get('email', 'N/A')}", ln=True)
    pdf.cell(0, 10, f"Phone: {data.get('phone', 'N/A')}", ln=True)
    pdf.cell(0, 10, f"Location: {data.get('location', 'N/A')}", ln=True)
    pdf.ln(5)
    
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(0, 10, "Professional Summary", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, data.get('summary', 'N/A'))
    pdf.ln(5)
    
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(0, 10, "Experience", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"{data.get('position', 'N/A')} at {data.get('company', 'N/A')}", ln=True)
    pdf.multi_cell(0, 10, data.get('experience_details', 'N/A'))
    pdf.ln(5)
    
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(0, 10, "Skills", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, data.get('skills', 'N/A'))
    pdf.ln(5)
    
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(0, 10, "Certifications", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, data.get('certifications', 'N/A'))
    pdf.ln(5)
    
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(0, 10, "Education", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, data.get('education', 'N/A'), ln=True)
    pdf.ln(5)
    
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(0, 10, "Languages", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, data.get('languages', 'N/A'))
    
    pdf_output = "resume.pdf"
    pdf.output(pdf_output)
    
    with open(pdf_output, "rb") as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read()).decode()
    
    return encoded_string

def get_pdf_download_link(encoded_pdf, filename="resume.pdf"):
    href = f'<a href="data:application/pdf;base64,{encoded_pdf}" download="{filename}">📄 Download Your Resume</a>'
    return href

def resume_form():
    with st.form("resume_form"):
        st.subheader("Fill in Your Details")
        
        # Personal Information
        name = st.text_input("Full Name")
        title = st.text_input("Job Title")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        location = st.text_input("Location")
        
        # Professional Summary
        summary = st.text_area("Professional Summary")
        
        # Experience
        company = st.text_input("Company Name")
        position = st.text_input("Position")
        experience_details = st.text_area("Job Responsibilities")
        
        # Skills
        skills = st.text_area("Skills (comma-separated)")
        
        # Certifications
        certifications = st.text_area("Certifications")
        
        # Education
        education = st.text_input("Education Details")
        
        # Languages
        languages = st.text_area("Languages Known (comma-separated)")
        
        submit = st.form_submit_button("Generate Resume")
        
        if submit:
            st.session_state['resume_data'] = {
                'name': name, 'title': title, 'email': email, 'phone': phone, 'location': location,
                'summary': summary, 'company': company, 'position': position, 'experience_details': experience_details,
                'skills': skills, 'certifications': certifications, 'education': education, 'languages': languages
            }
            st.success("Resume data saved! Now view your resume.")
            
            # Generate PDF for download
            encoded_pdf = generate_pdf(st.session_state['resume_data'])
            st.markdown(get_pdf_download_link(encoded_pdf), unsafe_allow_html=True)

if __name__ == "__main__":
    resume_form()
