import requests
import streamlit as st

# function to get the response from the url

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/coding_expert/invoke")
    json = {"input": {"topic": input_text}}

    return response.json()["output"]["content"]


def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke", json={"input": {"topic": input_text}}
    )

    return response.json()["output"]


# streamlit front-end

st.title("Langchain Project")  # title for the frontend application

input_text= st.text_input("Tell me what do you want to know about coding") # input for the OpenAI model

input_text1 = st.text_input("Write a poem on")


if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))




