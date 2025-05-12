import streamlit as st

def home():
    st.markdown("""
    <style>
    .block-container {
        padding-top: 7rem;
        padding-bottom: 5rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }

    .highlight-section {
        width: 100vw;
        margin-left: -5.5vw;
        background-image: url('https://images.indianexpress.com/2014/10/ayurveda-main.jpg');
        background-size: cover;
        background-position: center;
        filter: brightness(0.85);
        box-shadow: inset 0 0 0 1000px rgba(255, 255, 255, 0.25);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 40vh;
        padding: 0 4rem;
        text-align: center;
    }

    .highlight-section h2, .highlight-section p {
        color: #29153b;
        font-weight: bold;
        text-shadow: 1px 1px 2px #ffffff;
    }

    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(100px); }
        to { opacity: 1; transform: translateX(0); }
    }

    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-100px); }
        to { opacity: 1; transform: translateX(0); }
    }

    .section-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #ffffff;
        padding: 3rem;
        margin: 3rem 0;
        border-radius: 30px;
        box-shadow: 0 8px 20px rgba(41, 21, 59, 0.1);
        position: relative;
    }

    .section-container.right {
        animation: slideInRight 1s ease forwards;
    }

    .section-container.left {
        flex-direction: row-reverse;
        animation: slideInLeft 1s ease forwards;
    }

    .text-block {
        flex: 1;
        padding: 1rem;
    }

    .text-block h3 {
        font-size: 2rem;
        font-weight: bold;
        color: #3e3348;
        margin-bottom: 1rem;
    }

    .text-block p, .text-block ul {
        font-size: 1.1rem;
        color: #29153b;
        line-height: 1.6;
        margin-bottom: 1rem;
    }

    .text-block ul {
        list-style: disc;
        margin-left: 1.5rem;
    }

    .image-block {
        flex: 1;
        padding: 1rem;
        text-align: center;
    }

    /* 🖼️ Base Image Styling */
    .image-block img {
        max-width: 100%;
        border-radius: 20px;
        box-shadow: 0 0 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        
    }

    /* 🎨 Individual Image Styling */
    .about-img {
        border: 4px solid #9989ac;
        transform: rotate(-1deg);
        width: 70%;
        height: 170px;
        object-fit: cover;
        object-position: center;
        filter: blur(0.7px);
    }

    .works-img {
       border: 3px solid #d9cde8;
    #    transform: scale(1.05);
       width: 66%;
       height: 183px;
       object-position: center;
        transform: rotate(1deg);
    }

    .use-img {
        border: 3px solid #d9cde8;
        filter: grayscale(30%);
        transform: rotate(-1deg);
    
    }

    .curve-right, .curve-left {
        position: absolute;
        width: 120px;
        height: 120px;
        background: #e4d8f2;
        border-radius: 50%;
        z-index: -1;
    }

    .curve-right {
        right: -40px;
        top: -40px;
    }

    .curve-left {
        left: -40px;
        top: -40px;
    }
    </style>
    """, unsafe_allow_html=True)

    # 🔷 Banner Section
    st.markdown("""
    <div class='highlight-section'>
        <h2>Your Personalized Ayurvedic Health Assistant</h2>
        <p>CuraMate blends traditional Ayurveda with the power of AI to help you understand your symptoms and receive tailored remedies.</p>
    </div>
    """, unsafe_allow_html=True)

    # 🌱 About Section
    st.markdown("""
    <div class="section-container right">
        <div class="image-block">
            <img src="https://www.hopkinsmedicine.org/-/media/images/health/3_-wellness/integrative-medicine/ayurveda-hero.jpg" class="about-img" alt="About Image">
        </div>
        <div class="text-block">
            <h3>🌱 About CuraMate</h3>
            <p>CuraMate is a smart Ayurvedic assistant designed to bridge centuries-old wisdom with modern artificial intelligence. It provides personalized suggestions based on your selected symptoms.</p>
        </div>
        <div class="curve-right"></div>
    </div>
    """, unsafe_allow_html=True)

    # ⚙️ How It Works Section
    st.markdown("""
    <div class="section-container left">
        <div class="image-block">
            <img src="https://media.springernature.com/m685/springer-static/image/art%3A10.1038%2Fs41366-023-01369-3/MediaObjects/41366_2023_1369_Fig1_HTML.png" class="works-img" alt="How It Works">
        </div>
        <div class="text-block">
            <h3>⚙️ How It Works</h3>
            <p>Select your symptoms, and our AI model analyzes them to match with Ayurvedic conditions and remedies.</p>
        </div>
        <div class="curve-left"></div>
    </div>
    """, unsafe_allow_html=True)

    # 📋 How to Use Section
    st.markdown("""
    <div class="section-container right">
        <div class="image-block">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkLKJh48O7nshXbWysa2eKTy1vnZLHrGlFlfz76Popr6K7912VadD0Mq1eCaNxvQihPME&usqp=CAU" class="use-img" alt="How to Use">
        </div>
        <div class="text-block">
            <h3>📋 How To Use</h3>
            <ul>
                <li>Go to <strong>Smart Symptom Input</strong> in the navigation.</li>
                <li>Pick your symptoms from the list.</li>
                <li>Receive smart Ayurvedic recommendations instantly.</li>
            </ul>
        </div>
        <div class="curve-right"></div>
    </div>
    """, unsafe_allow_html=True)
