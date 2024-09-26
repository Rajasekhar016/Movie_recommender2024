import streamlit as st 
from langchain import PromptTemplate,LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

# Design the page...
st.title("Movie Recommender System..")
user_input=st.text_input("Enter the Movie Title,Genre or Keyword")