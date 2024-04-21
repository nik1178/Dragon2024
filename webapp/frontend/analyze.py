from openai import OpenAI

API_KEY = open("./webapp/frontend/API_KEY.txt", "r").read()

instructions = """
Answer in 50 words or less. You will receive a bunch of data points spread apart by one second. These points represent a cars parameters over time. These parameters are listed later. Your task is to analyze the data and provide a recommendation on how to improve fuel efficiency to drive as eco as possible. If you notice high rpm, high speed, etc. Recommend what can be done to improve fuel efficiency. At the end, give a score from 1-100 on how fuel efficient the ride was based on the data you are given (Be very harsh). If there is not enough data (under 50 data points), just say "Not enough data". REMEMBER THAT ALL DATA IS SPACED ONLY ONE SECOND APART. The parameters you will be analyzing are:"""
parameters = "speed(km/h), engine rpm, engine load (percentage from 0 to 255 equal to 0% to 100%), oil temperatur e(degrees Celsius °C)"
instructions1 = "Here are the data points you will be analyzing:"

def analyze(speed, engine_rpm, engine_load, oil_temp):
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