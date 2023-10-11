import os
import openai
from dotenv import find_dotenv, load_dotenv
from langchain.llms import OpenAI 
from langchain.chat_models import ChatOpenAI 
from langchain.schema import HumanMessage

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPEN_API_KEY")


llm_model = "gpt-3.5-turbo"

chat_model = ChatOpenAI(temperature=0.7, model=llm_model)

def get_completion(prompt, model=llm_model):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]