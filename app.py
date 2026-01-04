import streamlit as st
from streamlit_mic_recorder import speech_to_text
from hospital_finder import find_nearby_hospitals
from brain import speak, translate_and_extract

st.set_page_config(page_title="VocalCare", layout="centered")
st.title("🏥 VocalCare – Speak to Book")

# Step 1: Find hospitals
if st.button("🔍 Find Nearby Hospitals"):
    hospitals = find_nearby_hospitals(28.6139, 77.2090)

    for h in hospitals[:3]:
        if st.button(f"🏢 {h['name']}"):
            st.session_state.active_hospital = h

# Step 2: Voice-guided booking
if "active_hospital" in st.session_state:
    st.info(f"Selected Hospital: {st.session_state.active_hospital['name']}")

    audio = speak("Please tell me your full name")
    st.audio(audio, autoplay=True)

    user_text = speech_to_text(
        language="hi-IN",
        start_prompt="🎙️ Speak Your Name",
        stop_prompt="⏹️ Stop"
    )

    if user_text:
        name = translate_and_extract(user_text, "Full Name")
        st.success(f"Recognized Name: {name}")
