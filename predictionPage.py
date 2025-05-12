import streamlit as st
from app.symptoms import symptoms
import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from urllib.parse import urlencode
from data.ayurvedic_cure_data import ayurvedic_cures
from app.sym import data
from app.sym import NaiveBayes
from app.sym import message


def mainFunc():
    # Add custom CSS
    st.markdown("""
        <style>
            body {
                background-color: #f8f9fa;
                color: #333;
            }
            .stApp {
                background-image: linear-gradient(to right, #fdfbfb, #ebedee);
            }

            .highlight-section {
                 width: 100vw;
                 margin-left: -6.5vw;
                 background-image: url('https://jaims.in/public/journals/1/article_3687_cover_en_US.jpg');
                background-size: cover;
                background-position: center;
                filter: brightness(0.85);
                 box-shadow: inset 0 0 0 1000px rgba(255, 255, 255, 0.25);
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 40vh;
                padding: 0 13rem;
                text-align: center;
                background-position: 0% 72%;
                margin-bottom: 50px;

            }
                       
            .group-heading{
                font-size: 40px;
                font-weight: 800;
                margin-bottom: 0.4rem;
                margin-top: 20px;
                margin-left: 400px;
                margin-right: -180px;
                color:  #3b1e55;
                text-shadow: 1px 1px 2px #ffffff;
            }
            
            .group-title {
                font-size: 23px;
                font-weight: 650;
                color: #3b1e55;
                margin-bottom: 0.6rem;
                text-align: center;
                margin-left: 400px;
                margin-right: -185px;
                text-shadow: 1px 1px 2px #ffffff;
            }
            .group-text {
                margin-right: -180px;
                margin-left: 400px; 
                color: #32055b;
                margin-bottom: 50px;
                font-weight: 300;
            }
            .form-heading{
                font-size: 40px;
                font-weight: 600;
                text-align: center;
                color:  #3b1e55;
                text-shadow: 1px 1px 2px #ffffff;
            }
            .form-text{
                font-size: 20px;
                font-weight: 400;
                color: #3b1e55;
                text-align: center;
                text-shadow: 1px 1px 2px #ffffff;
                margin-bottom: 20px;
            }
          
            .stSelectbox label {
                color: #3e3348;
                margin-left: 180px;
                # font-weight: 800;
            }
            .stSelectbox div[data-baseweb="select"] {
                color: #000000 ;
                background-color: #ffffff;
                border-radius: 10px;
                padding: 3px;
            }
            .stSelectbox {
                margin-bottom: 0rem;
            }
            .stSelectbox > div {
                max-width: 800px;
                margin: auto;
            }
            .stButton > button {
                background-color: #725898;
                color: white;
                font-weight: bold;
                border-radius: 10px;
                padding: 0.5em 1em;
                transition: background-color 0.3s ease-in-out;
                margin-left: 510px;
                padding-left: 40px;
                padding-right: 40px;
                margin-top: 7px;
            }
            .stButton > button:hover {
                background-color: #5c3d85;
            }
            .custom-box {
                border: 2px solid #cbb9dd;
                border-radius: 15px;
                padding: 2rem;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
                width: 50%;
                margin: auto;
            }
           
            .group-footer {
                margin-top: 0.2rem;
                font-size: 14px;
                color: #6c757d;
                font-style: italic;
                text-align: center;
                margin-bottom: 2rem;
            }
            .st-bb {
                background-color: #e4d8f2;
            }
            .st-ba {
                border-bottom-color: #3e3348;
            }    
            .st-b6 {
                color: #86709a;
             }
            .st-b7 {
                border-left-color: #3e3348;
             }
            .st-b8 {
                border-right-color: #3e3348;
             }
            .st-b9 {
                border-top-color: #3e3348;
             }
            p{
                font-weight: 700;
               
            }
            .result-heading {
                font-size: 40px;
                font-weight: 600;
                text-align: center;
                color:  #3b1e55;
                text-shadow: 1px 1px 2px #ffffff;
                margin-top: 28px;
            }
            .disease-title {
               font-size: 30px;
               font-weight: bold;
               color: #8b1c42;
               text-align: center;
               margin-top: 10px;
            }
            .remedy-title {
                font-size: 18px;
                font-weight: 600;
                margin-top: 15px;
                color: #730d83;
                text-align: center;
            }
            .remedy-item {
               margin-left: 15px;
               color: #555;
               text-align: center;
            }
            .warning{
                color: #940a0a;
                padding: 10px 16px;
                border-radius: 5px;
                margin-top: 15px;
                font-weight: 500;
                margin-left: 362px;
            }
               
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='highlight-section'>
            <div class="group-heading"> Disease Prediction Assistant</div>
            <div class="group-title">Let us help you understand your health better</div>
            <div class="group-text"> Please select the symptoms that best describe how you're feeling. This will help us predict the most likely condition you may have. Choose up to five symptoms, and we'll provide the most probable disease along with Ayurvedic remedies that might help.</div>
        </div>        

    """, unsafe_allow_html=True)

    st.markdown('<div class="form-heading">Select the Symptoms You are Experiencing', unsafe_allow_html=True)
    st.markdown('<div class="form-text">Choose the symptoms that best describe how you are feeling', unsafe_allow_html=True)

    # Symptom Selection
    symptom1 = st.selectbox("Symptom 1", ["Select a Symptom"] + symptoms)
    symptom2 = st.selectbox("Symptom 2", ["Select a Symptom"] + symptoms)
    symptom3 = st.selectbox("Symptom 3", ["Select a Symptom"] + symptoms)
    symptom4 = st.selectbox("Symptom 4", ["Select a Symptom"] + symptoms)
    symptom5 = st.selectbox("Symptom 5", ["Select a Symptom"] + symptoms)

    st.markdown('<div class="group-footer">Note: Predicted Result will be AI-generated and should not replace professional medical advice.</div>', unsafe_allow_html=True)
    # Submit button
    if st.button("Submit"):
        predicted_disease = message(symptom1, symptom2, symptom3, symptom4, symptom5)
        if predicted_disease is None:
            st.markdown("<div class='warning'>Please select at least one valid symptom before submitting</div>", unsafe_allow_html=True)
        else:
            data['disease'] = predicted_disease

   
    
        st.markdown("<div style='border-top: 2px solid #123393; margin-top: 30px;'></div>", unsafe_allow_html=True)

        st.markdown("<div class='result-heading'>Prediction Result</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='disease-title'>Disease: {data.get('disease', 'Not Predicted')}</div>", unsafe_allow_html=True)

        st.markdown("<div class='remedy-title'>Suggested Ayurvedic Remedies</div>", unsafe_allow_html=True)

        remedies = ayurvedic_cures.get(data.get("disease", ""), [])
        if remedies:
                for i in remedies:
                    i_parts = i.split(":", 1)
                    search_query = urlencode({"q": i_parts[0]})
                    st.markdown(f"<div class='remedy-item'>🔎 <a href='https://www.google.com/search?q={search_query}' target='_blank'>{i}</a></div>", unsafe_allow_html=True)
        else:
                st.markdown("""
                    <div class='remedy-item'>
                    No immediate Ayurvedic remedies are available for this condition.<br>
                Please consult a certified medical professional for proper diagnosis and treatment.
               </div>
                """, unsafe_allow_html=True)

    # Display Results
    # st.write(f"**Predicted Disease:** {data.get('disease', 'Not Predicted')}")
    # st.write("**Ayurvedic Cure:**")
    # l = ayurvedic_cures.get(data.get('disease', []))
    # if l:
    #     for i in l:
    #         i_parts = i.split(":", 1)
    #         searchUrl = urlencode({"q": i_parts[0]})
    #         st.markdown(f"[🔎 {i}](https://www.google.com/search?q={searchUrl})")
    # st.markdown("<div class='result-section'>", unsafe_allow_html=True)