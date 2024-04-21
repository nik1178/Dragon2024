import openai
import streamlit as st

API_KEY = open("./API_KEY.txt", "r").read()

instructions = """
Answer in 50 words or less. You will receive a bunch of data points in the form of (x,y). These points represent a cars parameters over time. These parameters could be either speed, engine rpm, fuel consumption, etc. Your task is to analyze the data and provide a recommendation on how to improve fuel efficiency to drive as eco as possible. If you notice high rpm, high speed, etc. Recommend what can be done to improve fuel efficiency. The parameters you will be analyzing are:"""
parameters = ""
instructions1 = "Here are the data points you will be analyzing:"

def analyze(data, parameters):
    client = OpenAI(
        api_key=API_KEY,
    )
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=instructions + parameters + instructions1 + data,
    )
    
    message_text = response.choices[0].message.content
    print("ChatGPT response:")
    print(message_text)
    return message_text