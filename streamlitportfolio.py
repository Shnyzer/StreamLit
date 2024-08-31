import streamlit as st

st.set_page_config(layout="wide")

st.title("My First Streamlit App")

st.write("##")
st.subheader("Hello Everyone :wave: ")
st.title("My Portfolio")
st.write("Strong ability to gather and synthesize information while communicating results effectively and concisely in support of cooperative efforts.")

tabs = st.tabs(["Personal Data", "Skills", "Languages", "Projects"])

with tabs[0]:
    st.write("""
             - Name: Felix C. Vilocura II
             - Gender: Male
             - Civil Status: Single
             - Birthday: March 13, 2000
             - Birthplace: Cebu City
             - Region: Roman Catholic
             - Father: Felix C. Vilocura
             - Occupation: Civil Engineer, Business Management
             - Mother: Juliet C. Vilocura
             - Occupation: HouseWife""")
with tabs[1]:
    st.write("""
             - Open-Mindedness
             - Creativity
             - Motivation and Perseverance
             - Problem Solving and Resourcefulness
             - Critical Thinking
             - Leadership
             - Teamwork
             - Adaptibility""")
with tabs[2]:
    st.write("""
             - English
             - Tagalog
             - Cebuano 
             """)

with tabs[3]:
    col3, col4, col5 = st.columns(3)
    with col3:
        st.image("EnergyWise.png")
        st.write("""
                EnergyWise: Progressive Thinking towards Energy Efficiency
                """)
    with col4:
        st.image("HireHub.png")
        st.write("""
                 HireHub: Cebu Institute of Technology - University IT-Enabled Applicant Tracking System
                 """)
        
    with col5:
        st.image("TrafficScope.png")
        st.write("""
                 TrafficScope: Let's make your travel experience hassle-free!
                 """)
    
    
st.write("---")

st.title("Autobiography")
st.write("""
    I am Felix C. Vilocura II, born on March 13, 2000, and I live at 91-A F. Llamas St., Punta Princesa, Cebu City.
    I have been attending Cebu Institute of Technology - University since Kindergarten and am currently pursuing a Bachelor of Science in Information Technology.
    I have 5 brothers, and I am the third among them. My father is a Civil Engineer, and my mother, who has a background in Tourism, chose to be a housewife to guide us.
""")

st.write("""
    As a child growing up in Cebu City, I was fortunate to attend a well-regarded private school from kindergarten through high school and college.
    The people I met in my life instilled a strong educational and ethical philosophy that remains with me today. This foundation, along with the support of my family, educators, and friends, has helped me achieve my dreams.
    My favorite types of music are E.M.O and RAP, and my favorite foods include vegetables, calamares, and lechon. My favorite colors are dark colors.
""")

st.write("""
    One of my most unforgettable moments was during Senior High School when I had a lot of fun with my friends. We would often cut classes to play computer games, basketball, drink, or play billiards. Despite my grades suffering due to my lack of studying, I relied on my ability to remember discussions from school.
    I've learned from these experiences and have managed to stay on track despite the mistakes.
""")

col1, col2 = st.columns(2)

with st.container():
    with col1:
        check1 = st.checkbox("Education")

        if check1:
            
            st.write("""
                - Cebu Institute of Technology - University
                    - College - Bachelor of Science in Information Technology (Recent)
                - Cebu Institute of Technology - University
                    - Senior High School (2017 - 2019)
                - Cebu Institute of Technology - University
                    - Junior High School (2013 - 2017)
                - Cebu Institute of Technology - University
                    - Elementary (2007 - 2013)
            """)

    with col2:
        check2 = st.checkbox("Awards / Achievements")

        if check2:
            
             st.write("""
            Awards / Achievement
            -   March 09, 20222 
                -   Course Certificate - HCIP
            -   March 22, 2022
                -   Course Certificate - HCIA
            -   March 29, 2022
                -   Course Certificate - Information Representation & Data Organization
            -   April 05, 2022
                -   Course Certificate - HCIE
            -   May 04, 2023
                -   Certificate SOLOLEARN - Introduction to SQL
            -   May 04, 2023
                -   Certificate SOLORLEARN - PHP
            -   November 05, 2023 
                -   Certificate Kaggle - Data Visualization
                """)
