# app.py
import streamlit as st
from gpt import get_sentiment

# Streamlit UI
st.sidebar.title("Configuration 🔧")
api_key = st.sidebar.text_input("Enter your OpenAI API key 🔑:", type="password")

st.title("Sentiment Analysis with LLM")

text_input = st.text_area("Enter text to analyze:")

if st.button("Analyze Sentiment"):
    if not api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
    elif text_input:
        sentiment = get_sentiment(text_input, api_key).lower()
        
        if sentiment == "invalid api key":
            st.error("Invalid API key. Please check and try again.")
        elif "error" in sentiment.lower():
            st.error(f"An error occurred: {sentiment}")
        else:
            if "positive" in sentiment:
                st.success(f"Sentiment: {sentiment.capitalize()}", icon="✅")
            elif "negative" in sentiment:
                st.error(f"Sentiment: {sentiment.capitalize()}", icon="🚫")
            elif "neutral" in sentiment:
                st.warning(f"Sentiment: {sentiment.capitalize()}", icon="⚖️")
            else:
                st.info(f"Sentiment: {sentiment.capitalize()}")
    else:
        st.warning("Please enter some text to analyze.")
