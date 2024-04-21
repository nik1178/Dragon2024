from pathlib import Path
from openai import OpenAI
from playsound import playsound
import time
import os

API_KEY = open("./webapp/frontend/API_KEY.txt", "r").read()
# API_KEY=14
client = OpenAI(
    api_key=API_KEY,
)

speech_file_path = Path(__file__).parent / "speech.mp3"

def text_to_speech(text):
    global client
    global speech_file_path
    
    print("Converting text to speech...")
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )

    response.stream_to_file("speech.mp3")
    
    time.sleep(2)
    
    print('playing sound using  playsound')
    try:
        playsound("speech.mp3")
    except:
        playsound("speech.mp3")
    finally:
        try:
            os.remove("speech.mp3")
        except:
            pass
    

instructions = """
Answer in 50 words or less. You will receive a bunch of data points spread apart by one second. These points represent a cars parameters over time. These parameters are listed later. Your task is to analyze the data and provide a recommendation on how to improve fuel efficiency to drive as eco friendly as possible. If you notice high rpm, high speed, etc. Recommend what can be done to improve fuel efficiency. At the end, give a score from 1-100 on how fuel efficient the ride was based on the data you are given (Be very harsh). If there is not enough data (under 50 data points), just say "Not enough data". REMEMBER THAT ALL DATA IS SPACED ONLY ONE SECOND APART. The parameters you will be analyzing are:"""
parameters = "speed(km/h) (it just has to be steady, and below 150km/h), engine rpm, engine load (from 0 to 255), oil temperature (degrees Celsius °C)"
instructions1 = "Here are the data points you will be analyzing:"

def analyze(speed, engine_rpm, engine_load, oil_temp):
    global client
    
    print("Analyzing data...")
    client = OpenAI(
        api_key=API_KEY,
    )
    data = "speed: " + str(speed) + ", engine rpm: " + str(engine_rpm) + ", engine load: " + str(engine_load) + ", oil temperature: " + str(oil_temp)
    message={"role": "user", "content": (instructions + parameters + instructions1 + data)}
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[message]
    )
    
    message_text = response.choices[0].message.content
    print("ChatGPT response:")
    print(message_text)
    
    return message_text

def gameify(text):
    global client
    
    gameification_instructions = "Based on this response to someones driving, give them a rating of +1 or -1. Don't say anything else except the number. If you think they did well, give them a +1. If you think they did poorly, give them a -1. This was the description on their driving:"
    
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": (gameification_instructions + text)}]
    )
    message_text = response.choices[0].message.content
    
    print("ChatGPT response:")
    print(message_text)
    
    if message_text == "+1":
        return 1
    else :
        return -0.5
    

real_time_instructions = """You will analyze a ride in real time. You will receive a bunch of data points spread apart by one second. These points represent a cars parameters over time. These parameters are listed later. Your task is to analyze the data and provide small tips on how to improve fuel efficiency to drive as eco friendly as possible. Tell the driver if they are doing better or worse than before. If you notice high rpm, high speed, etc. Recommend what can be done to improve fuel efficiency. REMEMBER THAT ALL DATA IS SPACED ONLY ONE SECOND APART. THE RESPONSES SHOULD BE SHORT AND SWEET, 50 words or less. Make the response suited for speech. The parameters you will be analyzing are:"""
real_time_instructions += parameters

real_time_messages = []
real_time_messages.append({"role": "system", "content": (real_time_instructions)})

def real_time_analyze(speed, engine_rpm, engine_load, oil_temp, annoying, score):
    global real_time_messages
    global client
    
    print("Real time analysis of data...")
    
    annoying_prompt = ""
    if annoying:
        annoying_prompt = "Try to be as annoying and mean as possible. "
    else:
        annoying_prompt = "Try to be nice but stern."
    
    data = annoying_prompt + "Current data: "
    data += "speed: " + str(speed) + ", engine rpm: " + str(engine_rpm) + ", engine load: " + str(engine_load) + ", oil temperature: " + str(oil_temp)
    message={"role": "user", "content": (data)}
    real_time_messages.append(message)
    
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=real_time_messages
    )
    
    message_text = response.choices[0].message.content
    
    real_time_messages.append({"role": "assistant", "content": (message_text)})
    print("ChatGPT response:")
    print(message_text)
    
    text_to_speech(message_text)
    print("Finished real time analysis")
    
    # Get +1 or -0.5
    AI_response = gameify(message_text)
    if score[0] + AI_response > 0 and score[0] + AI_response < 100:
        score[0] += AI_response
    print("Score: ", score)
    
    # return message_text 