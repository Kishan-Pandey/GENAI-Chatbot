import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


import os
from dotenv import load_dotenv
load_dotenv()


#langsmith tracking

os.environ["LANGCHAHIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "QnA-GenAI-Project"

#prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that answers questions based on the provided context."),
        ("user", "Question: {question}"),
    ]
)

def generate_answer(question, api_key, llm, temperature, max_tokens):
    openai.api_key = api_key
    llm = ChatOpenAI(model = llm)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

#Streamlit UI
st.title("QnA Chatbot with LangChain and OpenAI")

#sidebar for settings
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("OpenAI API Key", type="password")


#dropdown to create various OPENAI models
llm = st.sidebar.selectbox(
    "Select LLM Model",
    ["gpt-4-turbo", "gpt-4o", "gpt-4"]
)

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.5)
max_tokens = st.sidebar.slider("Max Tokens", 50, 2000, 100)

#main interface 
st.write("Hi! Please ask your question below:")
user_input = st.text_input("Your Question:")

if user_input:
    response = generate_answer(user_input, api_key, llm, temperature, max_tokens)
    st.write("Answer:", response)
else:
    st.write("Please enter a question to get an answer.")
