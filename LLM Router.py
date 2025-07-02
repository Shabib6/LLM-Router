#LLM Router
#Built by Shabib

import os
from dotenv import load_dotenv
from openai import OpenAI

import anthropic
# from google import genai
import google.generativeai as genai

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_prompt = """You are an intelligent LLM Router. Your job is to analyze user queries and decide which model is best suited to answer the query.

You can choose from the following models:

1. GPT-4 (OpenAI): Best for general reasoning, creative writing, brainstorming, multi-tasking, and high-quality conversations across domains.
2. Gemini (Google): Best for real-world knowledge, factual accuracy, current events, and interpreting structured content like tables.
3. DeepSeek (DeepSeek Coder): Best for software development, code generation, algorithm writing, and debugging tasks.
4. LLaMA 3 (Meta via Ollama): Best for privacy-focused, general-purpose offline queries and thoughtful reasoning.
5. Mistral (Ollama): Best for fast, safe, and lightweight summarization, safe dialogue, and short-form Q&A.

Based on the user query, respond with only the model name most suitable for handling the task:
**"GPT-4"**, **"Gemini"**, **"DeepSeek"**, **"LLaMA 3"**, or **"Mistral"**.

Do not explain your choice.
Do not include any other text.

Examples:
User: "Summarize this 50-page contract" → Mistral  
User: "Write a function in Python to scrape weather data" → DeepSeek  
User: "Tell me who won the 2024 Champions League" → Gemini  
User: "Give me startup ideas for my final year project" → GPT-4  
User: "Explain artificial intelligence while I’m offline" → LLaMA 3  
User: "Create a REST API in Node.js" → DeepSeek  
User: "List India's top exports in 2023" → Gemini  
User: "Draft a creative sci-fi short story" → GPT-4  
User: "What is supervised learning?" → LLaMA 3"""


messages = {"role": "system","content":system_prompt}

import requests

def call_ollama(model_name: str, prompt: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model_name,     
            "prompt": prompt,        
            "stream": False        
        }
    )
    return response.json()["response"]  

def route_query(query:str) -> str:
    response = client.chat.completions.create(
        model ="gpt-4o",
        messages=[{"role": "system","content":system_prompt}, 
                  {"role": "user", "content": query}],
    )
    model_choice = response.choices[0].message.content.strip()
    VALID_MODELS = {"GPT-4", "Gemini", "DeepSeek", "Mistral","LLaMA 3"}
    return model_choice if model_choice in VALID_MODELS else "GPT-4"

def dispatch_query(model_choice: str, query: str):

    if model_choice == "Mistral":
        try:
            reply = call_ollama("mistral",query)
            print(reply)
        except Exception as e:
            print(f"Error Using Mistral {e}" )

    elif model_choice == "LLaMA 3":
        try:
            reply = call_ollama("llama3",query)
            print(reply)
        except Exception as e:
            print(f"Error Using LLaMA 3 {e}" )  

    elif model_choice == "Gemini":
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        
        model = genai.GenerativeModel("gemini-1.5-flash") 
        response = model.generate_content(query)
        print(response.text)

    elif model_choice == "DeepSeek":
        client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")

        system_prompt_deepseek = """You are a helpful assistant.
                You are an expert at code generation, software development, and debugging. "
                Given the user query, expertly resolve the query and return the response."""
        
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt_deepseek},
                {"role": "user", "content": query},
            ],
            stream=False
        )

        print(response.choices[0].message.content)

    else:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        system_prompt_chatgpt = """You are a helpful assistant.
        You are an expert at general reasoning, creative writing, multi-tasking, and high-quality conversations.
        Given the user query, expertly resolve the query and return the response."""
        response = client.chat.completions.create(
            model="gpt-4o",
            messages =[{"role": "system", "content": system_prompt_chatgpt},
                {"role": "user", "content": query}] 
        )
        print(response.choices[0].message.content)

while True:
    query = input(">> ")
    if query.lower() == "exit":
        break
    model_choice = route_query(query)
    print(f"Model chosen for the query: {model_choice}")
    dispatch_query(model_choice, query)

#model choice gives us the model name to use for the query
# if model_choice := route_query("What is the best model to answer this query?"):
#     print(f"Model chosen for the query: {model_choice}")
# else:   
#     print("No suitable model found for the query.")   