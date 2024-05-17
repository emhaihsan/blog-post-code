import os
import streamlit as st
import openai
from openai import OpenAI

# Retrieve the API key from the environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key:
    openai.api_key = openai_api_key
else:
    st.error("OpenAI API key not found. Please make sure the 'OPENAI_API_KEY' environment variable is set.")

client = OpenAI()

# Function to translate text using ChatGPT
def translate_text(text, source_lang, target_lang):
    messages = [
        {"role": "system", "content": f"You are a helpful translator that translates from {source_lang} to {target_lang}."},
        {"role": "user", "content": text}
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    translation = response.choices[0].message.content
    return translation

# Streamlit interface
st.title("Simple Translator")

source_lang = st.selectbox("Select Source Language", ["English", "Indonesian", "Spanish", "French", "German", "Chinese"], index=0)
target_lang = st.selectbox("Select Target Language", ["English", "Indonesian", "Spanish", "French", "German", "Chinese"], index=1)

text_to_translate = st.text_area("Enter Text to Translate")

if st.button("Translate"):
    if text_to_translate:
        translation = translate_text(text_to_translate, source_lang, target_lang)
        st.write("Translation Result:")
        st.write(translation)
    else:
        st.write("Please enter text to translate.")
