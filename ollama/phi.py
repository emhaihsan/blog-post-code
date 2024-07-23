from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_ollama import ChatOllama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the queries"),
    ("user", "Question:{question}"),
])

# Streamlit framework

st.set_page_config(
    page_title="Chatbot",
    page_icon=":robot:"
)

st.header("Phi 3 Chatbot")

input_text = st.text_input("Search the topic u want")

# openAI LLM
llm =ChatOllama(model="phi3")
output_parser = StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))