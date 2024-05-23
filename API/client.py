# # import requests
# # import streamlit as st


# # def get_openai_response(input_text):

# #     # Fixing the request body and sending it correctly
# #     url = "http://localhost:8000/coding_expert/invoke"
# #     payload = {"topic": input_text}
# #     headers = {"Content-Type": "application/json"}
# #     response = requests.post(url, json=payload, headers=headers)

# #     # Properly handling the response and extracting the content
# #     if response.status_code == 200:
# #         return response.json().get("output", "No response from model")
# #     else:
# #         return f"Error: {response.text}"


# # def get_ollama_response(input_text):
# #     url = "http://localhost:8000/AI_Expert/invoke"
# #     headers = {"Content-Type": "application/json"}
# #     payload = {"topic": input_text}
# #     try:
# #         response = requests.post(
# #             url, json=payload, headers=headers
# #         )  # Ensure this uses 'post'
# #         response.raise_for_status()
# #         data = response.json()
# #         return data.get("AI_Expert", "No response received from the model")
# #     except requests.exceptions.HTTPError as http_err:
# #         error_message = response.json()
# #         return f"HTTP error occurred: {http_err}; Details: {error_message}"
# #     except Exception as err:
# #         return f"An error occurred: {err}"


# # # Streamlit front-end setup
# # st.title("Langchain Project")  # Title for the frontend application

# # input_text = st.text_input(
# #     "Ask me Anything about Coding "
# # )  # Input for the OpenAI model


# # input_text1 = st.text_input(
# #     "I am an AI Expert ask me anything related to it"
# # )  # Input for the Ollama model


# # if input_text:
# #     response = get_openai_response(input_text)
# #     st.write(response)

# # if input_text1:
# #     ollama_response = get_ollama_response(input_text1)
# #     st.write(ollama_response)

# import requests
# import streamlit as st


# def get_openai_response(input_text):
#     response = requests.post(
#         "http://localhost:8000/coding_expert/invoke",
#         json={"input": {"topic": input_text}},
#     )

#     return response.json()["output"]["content"]


# def get_ollama_response(input_text):
#     response = requests.post(
#         "http://localhost:8000/ai_expert/invoke", json={"input": {"topic": input_text}}
#     )

#     return response.json()["output"]

#     ## streamlit framework


# st.title("Langchain API Demo Project")
# # input_text = st.text_input("Ask me anything on")
# input_text1 = st.text_input("Ask me anything  on")

# # if input_text:
# #     st.write(get_openai_response(input_text))

# if input_text1:
#     st.write(get_ollama_response(input_text1))

import requests
import streamlit as st


# def get_openai_response(input_text):
#     response = requests.post(
#         "http://localhost:8000/essay/invoke", json={"input": {"topic": input_text}}
#     )

#     return response.json()["output"]["content"]


def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke", json={"input": {"topic": input_text}}
    )

    return response.json()["output"]

    ## streamlit framework


st.title("Langchain Demo With LLAMA2 API")
# input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")

# if input_text:
#     st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))
