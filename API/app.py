# importing the libraries
import os
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import uvicorn


load_dotenv()

# loading the keys
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Langsmith Tracking dependencies
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


# creating the API

app = FastAPI(
    title="Langchain Server", version="1.0", description="This is a Simple API Server"
)

# adding routes to different LLM models
add_routes(app, ChatOpenAI(), path="/openai")  # OpenAI route

# openai Model
model = ChatOpenAI()

# LLAMA3 model
llm = Ollama(model="llama3")

# prompt Templates for the LLM models
prompt_openai_model = ChatPromptTemplate.from_template(
    "You are a coding Expert with an experience of 25+ years, you need to help the user on the {topic}"
)
prompt_llama_model = ChatPromptTemplate.from_template(
    "Write a poem on {topic} in 100 words"
)


# add route

add_routes(
    app, prompt_openai_model, path="/coding_expert"
)  # route for coding using OPENAI_API

add_routes(app, prompt_llama_model, path="/poem")


# main
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)



