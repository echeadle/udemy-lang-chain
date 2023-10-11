import os
import openai
from dotenv import find_dotenv, load_dotenv
from langchain.llms import OpenAI 
from langchain.chat_models import ChatOpenAI 
from langchain.schema import HumanMessage

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

llm_model = "gpt-3.5-turbo"

# OpenAI Completion Endpoint
def get_completion(prompt, model=llm_model):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

# Translate text, review
customer_review = """
 Your product is terrible!  I don't know how 
 you were able to get this to the market.
 I don't want this! Actually no one should want this.
 Seriously!  Give me money now!
 
"""
tone = """ Proper British English in a nice, warm, respectful tone """
language = "Turkish"
promp = f"""
    Rewrite the following {customer_review}  in {tone}, and then
    please translate the new review message into {language}.
"""

if __name__ == "__main__":

    rewrite = get_completion(prompt=promp)
    print(rewrite)
    