import streamlit as st

# Set page configuration for a wider layout and custom title
st.set_page_config(page_title="Life 3.0 Voice Cloning", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for a prettier look
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .header {
        color: #2c3e50;
        text-align: center;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subheader {
        color: #34495e;
        text-align: center;
        font-size: 1.5em;
        margin-bottom: 10px;
    }
    .description {
        color: #7f8c8d;
        font-size: 1.1em;
        line-height: 1.6;
        text-align: justify;
        margin-bottom: 20px;
    }
    .button {
        background-color: #3498db;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
        margin: 5px;
    }
    .button:hover {
        background-color: #2980b9;
    }
    </style>
    """, unsafe_allow_html=True)

# Header and Image
st.markdown('<div class="header">Life 3.0 Voice Cloning Project</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">By Sarmad Mahmood</div>', unsafe_allow_html=True)
st.image("https://example.com/life3_cover.jpg", caption="Cover of Life 3.0 by Max Tegmark", use_column_width=True, output_format="auto")

# Project Description
st.markdown('<div class="description">Welcome to my Generative AI assignment! This project transforms text from *Life 3.0: Being Human in the Age of Artificial Intelligence* by Max Tegmark into personalized audio narration using ElevenLabs. I extracted text from a 440-page PDF, converted it to speech with a default voice, and cloned my own voice to create a unique narration. Challenges like quota limits were overcome by splitting audio and upgrading my plan. Explore the code on GitHub: [Link to Repo]</div>', unsafe_allow_html=True)

# Audio Playback Section
st.markdown('<h3 style="color: #2c3e50; text-align: center;">Listen to the Voices</h3>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("Listen to Random Voice", key="random_voice"):
        audio_file = open("random_speech.mp3", "rb")
        st.audio(audio_file, format="audio/mp3")

with col2:
    if st.button("Listen to My Voice", key="my_voice"):
        audio_file = open("my_voice_speech.mp3", "rb")
        st.audio(audio_file, format="audio/mp3")

# Footer
st.markdown('<div style="text-align: center; color: #7f8c8d; margin-top: 20px;">© 2025 Sarmad Mahmood | Built with Streamlit</div>', unsafe_allow_html=True)