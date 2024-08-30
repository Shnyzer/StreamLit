import streamlit as st 
import numpy as np
import pandas as pd 
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout= "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_code = load_lottieurl ("https://lottie.host/677afcc3-42fb-4602-a75a-6d754897c22b/pFsY797vh1.json")
image = Image.open("C:\\Users\\User\\Downloads\\MyFirstStreamLitApp\\Hirehub.png")


st.title("My First Streamlit App")

st.write("##")
st.subheader("Hello Everyone :wave: ")
st.title("My Portfolio")
st.write("Strong Ability to gather and synthesize information while communicating results effectively and concisely in support of cooperate efforts")
st.write("---")

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About', 'Projects', 'Contact'],
        default_index=0,
        icons = ['person', 'code-slash', 'chat-left-text-fill'],
        orientation= 'horizontal',
    )

if selected == 'About':
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Felix C. Vilocura II")
            st.title("BSIT Student")
        with col2:
            st.write("##")
            st_lottie(lottie_code)

    st.write("---")
    
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("""
            Education
            - Cebu Institute of Technology - University
                -   College - Bachelor of Science Information of Technology 
                -   Recent 
            - Cebu Institute of Technology - University 
                -   Senior High School 
                -   2017 - 2019
            - Cebu Institute of Technology - University 
                -   Junior High School 
                -   2013 - 2017
            - Cebu Institute of Technology - University
                -   Elementary
                -   2007 - 2013
                """)
        with col4:
            st.subheader("""
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
if selected == 'Projects':
    with st.container():
        st.header("My Projects")
        st.write("##")
        col5, col6 = st.columns({1,2})
        with col5:
            st.image(image)
        with col6:
            st.subheader("HireHub")
            st.write("""HireHub: Cebu Institute of Technology - University 
                    IT-Enabled 
                    Applicant Tracking 
                    System""")

elif selected == 'Contact':
    st.header("Contact Me")
    st.write("You can reach me at my email: fvilocuraii@gmail.com")
        
