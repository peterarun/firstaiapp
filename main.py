import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

st.header(" A Tweet Generataro")
st.subheader("Generate some tweets with Generative AIIII")

topic = st.text_input("Topic")
number = st.number_input("Tweet Count", min_value=1, max_value=5, value=1, step=1)

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

# Create prompt template for generating tweets
tweet_template = "Give me {number} tweets on {topic}"

tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic'])

# Create LLM chain using the prompt template and model
tweet_chain = tweet_prompt | gemini_model

# Example of using the LLM chain

if st.button("Generate"):
    response = tweet_chain.invoke({"number": number, "topic": topic})
    st.write(response.content)
