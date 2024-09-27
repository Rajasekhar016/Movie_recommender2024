import streamlit as st  # type: ignore
from langchain import PromptTemplate,LLMChain # type: ignore
from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
import google.generativeai as genai

# Import The Local Environment
from dotenv import load_dotenv # type: ignore
import os
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))# type: ignore

# Design the page...
headers={"authorization":st.secrets["GOOGLE-API-KEY"],
         "content-type":"application/json"}
st.title("Movie Recommender System..")
user_input=st.text_input("Enter the Movie Title,Genre or Keyword")

# Prompt Template
demo_template ='''Based on the {user_input} provide the Movie recommendations'''
template=PromptTemplate(input_variables=['user_input'],template=demo_template)

# Google Gemini Model...
llm=ChatGoogleGenerativeAI(model='gemini_pro',api_key=os.getenv('GOOGLE-API-KEY'))

if user_input:
    prompt=template.format(user_input =user_input)
    recommendations=llm.predict(text=prompt)
    st.write(f'Recommendations for you:\n {recommendations}')
else:
    st.write("Please enter the Movie Name")