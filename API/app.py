# # importing the libraries
# import os
# from fastapi import FastAPI, HTTPException
# from fastapi.responses import JSONResponse
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
# from langserve import add_routes
# from dotenv import load_dotenv
# from langchain_community.llms import Ollama
# from pydantic import BaseModel
# import uvicorn
# import logging

# load_dotenv()

# # loading the keys
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# # Langsmith Tracking dependencies
# os.environ["LANGCHAIN_TRACKING_V2"] = "true"

# # creating the API
# app = FastAPI(
#     title="Langchain Server", version="1.0", description="This is a Simple Langserve API Server"
# )

# class CodingExpert(BaseModel):
#     topic: str


# class AI_Expert(BaseModel):
#     topic: str


# # openai Model
# openai_model = ChatOpenAI()

# # LLAMA3 model
# llama_model = Ollama(model="llama3")

# # prompt Templates for the LLM models
# # prompt_openai_model = ChatPromptTemplate.from_template(
# #     "You are a coding Expert with an experience of 25+ years, you need to help the user on the {topic}"
# # )
# prompt_llama_model = ChatPromptTemplate.from_template(
#     "You are an expert in Machine Learning and AI, help the user on {topic} and explain it in 100 words"
# )

# # Add routes using the add_routes function from langserve
# # add_routes(app, ChatOpenAI(), path="/openai")  # Route for OpenAI

# add_routes(app, Ollama(), path="/Ollama")  # Route for the Ollama

# # add_routes(
# #     app, prompt_openai_model | openai_model, path="/coding_expert"
# # )  # Route for coding using OpenAI API

# add_routes(
#     app, prompt_llama_model | llama_model, path="/ai_expert"
# )  # Route for poetry using LLAMA

# # Main
# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)


from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="Langchain Server", version="1.0", decsription="A simple API Server"
)

# add_routes(app, ChatOpenAI(), path="/openai")
# model = ChatOpenAI()
##ollama llama2
add_routes(app, Ollama(), path="/ollama")

llm = Ollama(model="llama2")

# prompt1 = ChatPromptTemplate.from_template(
#     "Write me an essay about {topic} with 100 words"
# )
prompt2 = ChatPromptTemplate.from_template(
    "Write me an poem about {topic} for a 5 years child with 100 words"
)

# add_routes(app, prompt1 | model, path="/essay")

add_routes(app, prompt2 | llm, path="/poem")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
