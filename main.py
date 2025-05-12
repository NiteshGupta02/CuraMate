import streamlit as st
from app.homepage import home
from app.predictionPage import mainFunc
from app.ayurvedicRemediesPage import ayurRemedies



# Configure page
st.set_page_config(page_title="CuraMate", layout="wide")

# Custom CSS and HTML Navigation
st.markdown("""
    <style>
        /* App Background */
        .stApp {
            background-color: #f1f4f8; /* light cool gray-blue */
            color: #1a1a1a;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Top Navigation Bar */
        .topnav {
            position: fixed;
            top: 3rem;
            left: 0;
            right: 0;
            width: 100%;
            z-index: 9999;
            overflow: hidden;
            background-color: #3e3348; /* dark bluish navbar */
            padding: 0.6rem 1.5rem 0rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        }

        .logo-title {
            display: flex;
            align-items: center;
            
        }

        .logo-title img {
            height: 25px;
            margin-right: 10px;
            border-radius: 100px;
        
        }

        .logo-title h3 {
            margin: 0;
            color: #ffffff;
        }

        .nav-links a {
            margin-left: 20px;
            text-decoration: none;
            color: #ffffff;
            font-weight: 600;
            font-size: 16px;
            cursor: pointer;
        }

        .nav-links a:hover {
            text-decoration: underline;
        }
             .nav-links button {
            margin-left: 20px;
            background-color: transparent;
            color: white;
            border: none;
            font-weight: bold;
            font-size: 16px;
            cursor: pointer;
        }

        .nav-links button:hover {
            text-decoration: underline;
        }


        .section-container {
            padding: 3rem 2rem;
        }

    </style>

    <!-- Top Navigation -->
    <div class="topnav">
        <div class="logo-title">
            <img src="https://wallpapershome.com/images/pages/ico_v/25815.jpg" alt="CuraMate Logo">
            <h3>CuraMate</h3>
        </div>
        <div class="nav-links">
            <a href="?home">Home</a>
            <a href="?symptoms">Smart Symptom Input</a>
            <a href="?remedies">Ayurvedic Remedies</a>
        </div>
    </div>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "home"

# Read query params to simulate navigation
nav_clicked = st.query_params
if "home" in nav_clicked:
    st.session_state.page = "home"
elif "symptoms" in nav_clicked:
    st.session_state.page = "symptoms"
elif "remedies" in nav_clicked:
    st.session_state.page = "remedies"
# Page rendering
if st.session_state.page == "home":
    home()  # now using the separate file

elif st.session_state.page == "symptoms":
    
    mainFunc()  # call the function to render it    

elif st.session_state.page == "remedies":
    
    ayurRemedies()  # call the function to render it      

