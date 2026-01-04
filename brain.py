import os
from gtts import gTTS
from langchain_nvidia_ai_endpoints import ChatNVIDIA

llm = ChatNVIDIA(model="meta/llama-3.1-70b-instruct")

def speak(text, lang='hi'):
    # Converts text to audio file for the user to hear
    tts = gTTS(text=text, lang=lang)
    tts.save("instruction.mp3")
    return "instruction.mp3"

def translate_and_extract(native_text, field_name):
    # Translates user's answer into the English value needed for the form
    prompt = f"The user said '{native_text}' in their native language. Extract the relevant information for the form field '{field_name}' in English."
    response = llm.invoke(prompt)
    return response.content.strip()