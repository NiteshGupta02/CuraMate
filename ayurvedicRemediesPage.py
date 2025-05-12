import streamlit as st
from data.ayurvedic_cure_data import ayurvedic_cures



def ayurRemedies():

    st.markdown("""
        <style>
                .highlight-section {
                 width: 100vw;
                 margin-left: -5.5vw;
                 background-image: url('https://www.metropolisindia.com/upgrade/blog/upload/2020/09/ayurvedic-remedies-for-cold-cough.png');
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
                margin-bottom: -0.6rem;
                margin-top: 20px;
                margin-left: -175px;
                margin-right: 480px;
                color:  #271339;
                text-shadow: 1px 1px 2px #ffffff;
            }
            
            .group-text {
                font-size: 20px;
                font-weight: 600;
                color: #0e2657;
                margin-bottom: 0.6rem;
                margin-left: -262px;
                margin-right: 402px;
                margin-top: 15px;
                # text-shadow: 1px 1px 2px #ffffff;
            }
        </style>
    """, unsafe_allow_html=True)        

    st.markdown("""
        <div class='highlight-section'>
            <div class="group-heading"> Ayurvedic Remedies for Common Conditions </div>
            <div class="group-text">Natural Healing Suggestions for various health conditions</div>
        </div>        

    """, unsafe_allow_html=True)
   

    for disease in sorted(ayurvedic_cures.keys()):
        with st.expander(f"💠 {disease}"):
            for remedy in ayurvedic_cures[disease]:
                st.markdown(f"• {remedy}")

