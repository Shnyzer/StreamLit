import streamlit as st
from PIL import Image

# Configure the layout to be wide
st.set_page_config(layout="wide")

# Load the image
image = Image.open("C:\\Users\\User\\Downloads\\MyFirstStreamLitApp\\Hirehub.png")

# Main title and introductory text
st.title("My First Streamlit App")
st.write("##")
st.subheader("Hello Everyone :wave:")
st.write("Strong Ability to gather and synthesize information while communicating results effectively and concisely in support of corporate efforts")
st.write("---")

# Create a sidebar for navigation
selected = st.sidebar.selectbox(
    "Select a section",
    ("About", "Projects", "Contact")
)

# Content for the 'About' section
if selected == 'About':
    st.header("About Me")
    st.subheader("I am Felix C. Vilocura II")
    st.write("BSIT Graduate")

    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Education")
        st.write("""
        - Cebu Institute of Technology - University
            - College - Bachelor of Science Information Technology 
            - Recent Graduate
        - Cebu Institute of Technology - University 
            - Senior High School 
            - 2017 - 2019
        - Cebu Institute of Technology - University 
            - Junior High School 
            - 2013 - 2017
        - Cebu Institute of Technology - University
            - Elementary
            - 2007 - 2013
        """)
    with col2:
        st.subheader("Awards / Achievements")
        st.write("""
        - March 09, 2022: Course Certificate - HCIP
        - March 22, 2022: Course Certificate - HCIA
        - March 29, 2022: Course Certificate - Information Representation & Data Organization
        - April 05, 2022: Course Certificate - HCIE
        - May 04, 2023: Certificate SOLOLEARN - Introduction to SQL
        - May 04, 2023: Certificate SOLOLEARN - PHP
        - November 05, 2023: Certificate Kaggle - Data Visualization
        """)

# Content for the 'Projects' section
elif selected == 'Projects':
    st.header("My Projects")
    st.write("##")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(image)
    with col2:
        st.subheader("HireHub")
        st.write("""
        HireHub: Cebu Institute of Technology - University 
        IT-Enabled Applicant Tracking System
        """)

# Content for the 'Contact' section
elif selected == 'Contact':
    st.header("Contact Me")
    st.write("You can reach me at my email: felix.vilocura@example.com")
