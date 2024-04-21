from flow_py_sdk import flow_client
import flet as ft
import time
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from flet.matplotlib_chart import MatplotlibChart
import threading
import com_reader
from pymongo.mongo_client import MongoClient
import analyze
import sys
from flet_core.control_event import ControlEvent
import json
from flow_py_sdk import flow_client
from flet import TextField, Checkbox, ElevatedButton

matplotlib.use("svg")
score = [100]
annoying = False


def main(page: ft.Page):
    
    

    global stop_bool
    stop_bool = False
    global username
    username = "notloggendin"
    global txt_stop
    txt_stop = "Start ride"
    global txt_login
    txt_login = "Login"
    global button_stop
    global button_login
    global x_data
    global y1_data, y2_data, y3_data, y4_data
    
    global previous_analysis_time
    global score
    global annoying
    
    global start_time
    start_time = time.time()

    global loginchoice
    loginchoice = 0 # 0 = not logged in, 1 = logged in
    
    def go_with_the_flow():
        #posl tolk kot je score coinov v wallet od userja
        print("sending reward " + score)
        #async with flow_client(
            #host=ctx.access_node_host, port=ctx.access_node_port
        #) as client:
            #block = await client.get_latest_block(is_sealed=False)

    #page.theme_mode = ft.ThemeMode.SYSTEM
    page.bgcolor = "#101210"
    page.title = "rAId"
    page.scroll = "adaptive"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {
        
    }

    login_interface = ft.Card(visible=False)
    login_text = ft.Text(size=15, weight=ft.FontWeight.W_500, text_align=ft.TextAlign.START)

    page.add(
        ft.Text("R", size=50, weight=ft.FontWeight.W_500, 
                spans=[ft.TextSpan("AI", ft.TextStyle(size=50, weight=ft.FontWeight.W_700, color="#3c8062")), ft.TextSpan("d", ft.TextStyle(size=50, weight=ft.FontWeight.W_500))]),
    )
    
    page.update()

    def append_data_to_json(file_path, new_data):
        # Try to load existing data
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                assert isinstance(data, list)  # Ensure it is a list as expected
        except FileNotFoundError:
            data = []  # If not found, start with an empty list
        except json.JSONDecodeError:
            raise Exception("File is not in valid JSON format")
        
        # Append new data to the list
        data.append(new_data)

        # Write updated data back to the file
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def checkjson(new_data):
        filename = 'login.json'  # Path to the JSON file containing the user data

        # Load JSON data from the file
        try:
            with open(filename, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print("File not found.")
            return
        except json.JSONDecodeError:
            print("Error decoding JSON.")
            return

        # Iterate through each user in the list
        for user in users:
            # Retrieve 'username' or 'name' based on available keys
            username = user.get('name') or user.get('username')  # Handle variations in key naming
            password = user['password']  # It is assumed that every entry will have a 'password' key

            print(f"Username: {username}, Password: {password}")
            if username == new_data['username'] and password == new_data['password']:
                return 0
            elif username == new_data['username']:
                return 1
        
        return 2

    filename = 'login.json'

    text_username: TextField = ft.TextField(label="Username", text_align=ft.TextAlign.LEFT, width=200)
    text_password: TextField = ft.TextField(label="Password", text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_signup: Checkbox = ft.Checkbox(label="I agree to stuff", value=False)
    button_submit: ElevatedButton = ft.ElevatedButton("Sign up", width=200, bgcolor="blue", color="white", disabled=True)

    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True

        page.update()

    def submit(e: ControlEvent) -> None:
        global username
        print("Username:", text_username.value)
        print("Password:", text_password.value)
        new_user = {"username": text_username.value, "password": text_password.value}
        
        if (checkjson(new_user) == 0): ### kle
            login_interface.visible = False
            login_text.value = "Welcome back " + text_username.value + ", here is a summary of all your rides:"
            page.update()
        elif (checkjson(new_user) == 1):
            #wrong password
            login_text.value = "Wrong username or password, please try again"
            page.update()
            #page.clean()
        else:
            #create new user
            login_text.value = "Welcome " + text_username.value + ", we will start tracking your rides"
            append_data_to_json(filename, new_user)
            page.update()

    
    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

    

    def send_data(e):
        global stop_bool
        global txt_stop, button_stop
        global x_data
        global y1_data, y2_data, y3_data, y4_data
        global username
        global start_time
        start_time = time.time()
        
        
        if stop_bool:
            stop_bool = False
            txt_stop="Start ride"
            
            json_data = {
                "username": username,
                "x": x_data,
                "y1": y1_data,
                "y2": y2_data,
                "y3": y3_data,
                "y4": y4_data
            }
            AI_response = analyze.analyze(y1_data, y2_data, y3_data, y4_data)
            analysis_field.value = AI_response
            page.update()
            try:
                uri = "mongodb+srv://dragon:dragonhack123@dh.xbqmeva.mongodb.net/?retryWrites=true&w=majority&appName=DH"
                client = MongoClient(uri)
                db = client["dh"]
                collection = db["raid"]
                insert_result = collection.insert_one(json_data)
            except Exception as e:
                print("An error occurred:", e)
    
        else:
            analysis_field.value = ""
            page.update()
            stop_bool = True
            txt_stop="End & Save ride"
        
        # AI_response = analyze.analyze(y1_data, y2_data, y3_data, y4_data)
        
        button_stop.text = txt_stop
        button_stop.update()

    def view(e):
        try:
            uri = "mongodb+srv://dragon:dragonhack123@dh.xbqmeva.mongodb.net/?retryWrites=true&w=majority&appName=DH"
            client = MongoClient(uri)
            db = client["dh"]
            collection = db["raid"]
            insert_result = collection.insert_one(json_data)
        except Exception as e:
            print("An error occurred:", e)
    

    def login(e):
        global txt_login
        global username
        global button_login
        
        if username == "notloggendin":
            txt_login = "Logout"
            page.route = "/auth0"
            page.update()
        else:
            username = "notloggendin"
            txt_login = "Login"
        print(txt_login)
        button_login.text = txt_login
        button_login.update()
        
    def loginbuttonfunction(e):
        global loginchoice

        if (loginchoice == 0):
            login_interface.visible = True
            login_interface.content=ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Column(
                                    [text_username,
                                    text_password,
                                    checkbox_signup,
                                    button_submit]
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    )
            page.update()
            loginchoice = 1
        else:
            #ft.Card
            login_interface.visible = False
            loginchoice = 0
            page.update()

    def annoying_switch(e):
        global annoying
        if annoying:
            annoying = False
        else:
            annoying = True

    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    fig3, ax3 = plt.subplots()
    fig4, ax4 = plt.subplots()
    x_data = []
    y1_data, y2_data = [], []
    y4_data, y3_data = [], []

    graf1 = MatplotlibChart(fig1, isolated=True, expand=True, transparent=True)
    graf2 = MatplotlibChart(fig2, isolated=True, expand=True, transparent=True)
    graf3 = MatplotlibChart(fig3, isolated=True, expand=True, transparent=True)
    graf4 = MatplotlibChart(fig4, isolated=True, expand=True, transparent=True)
    
    page.add(
        ft.Row([
            graf1,
            graf2
        ]),
        ft.Row([
            graf3,
            graf4
        ])
    )

    button_stop = ft.ElevatedButton(text=txt_stop, on_click=send_data)
    button_loginchoice = ft.ElevatedButton(text="Log in/Sign up", on_click=loginbuttonfunction)
    button_login = ft.ElevatedButton(text=txt_login, on_click=login)
    button_history = ft.ElevatedButton(text="View history", on_click=view)

    page.add(
        ft.Row([
            ft.Text("Click on this button to start analysis: ", size=20, weight=ft.FontWeight.W_500),
        ]),
        button_stop,
        #button_login, #nevemkajto nrid
        button_history,
        ft.Row([
            ft.Text("Click on this button to log in or sign up: ", size=20, weight=ft.FontWeight.W_500),
        ]),
        button_loginchoice,

        login_interface,
        ft.Row([login_text])
    )

    
    page.add(
        ft.Switch(
            label="Annoying", label_position=ft.LabelPosition.RIGHT,
            on_change=annoying_switch
        )
    )
    
    score_label = ft.TextField(label="Score", disabled=True, value=str(score[0]))
    page.add(score_label)
    analysis_field = ft.TextField(label="Analysis", disabled=True, value="", multiline=True, max_lines=5555)
    page.add(analysis_field)

    page.update()

    def update_graph1():        
        ax1.clear()
        ax1.plot(x_data, y1_data, color="#a2faa2")
        ax1.set_ylim(0, 255)
        ax1.set_xlabel('Time [s]', color="white")
        ax1.set_ylabel('Velocity [km / h]', color="white")
        ax1.xaxis.label.set_color('white')
        ax1.tick_params(axis='x', colors='white')
        ax1.tick_params(axis='y', colors='white')
        ax1.spines['bottom'].set_color('white')  
        ax1.spines['left'].set_color('white') 
        ax1.spines['right'].set_color('#101210')  
        ax1.spines['top'].set_color('#101210')    


    def update_graph2():          
        ax2.clear()
        ax2.plot(x_data, y2_data, color="#ff879d")
        ax2.set_ylim(0, 8000)
        ax2.set_xlabel('Time [s]', color="white")
        ax2.set_ylabel('RPM Engine', color="white")
        ax2.tick_params(axis='x', colors='white')
        ax2.tick_params(axis='y', colors='white')
        ax2.spines['bottom'].set_color('white')  
        ax2.spines['left'].set_color('white') 
        ax2.spines['right'].set_color('#101210')  
        ax2.spines['top'].set_color('#101210')   

    def update_graph3():           
        ax3.clear()
        ax3.plot(x_data, y3_data, color="#a3c2ff")
        ax3.set_ylim(0, 100)
        ax3.set_xlabel('Time [s]', color="white")
        ax3.set_ylabel('Engine load [%]', color="white")
        ax3.tick_params(axis='x', colors='white')
        ax3.tick_params(axis='y', colors='white')
        ax3.spines['bottom'].set_color('white')  
        ax3.spines['left'].set_color('white') 
        ax3.spines['right'].set_color('#101210') 
        ax3.spines['top'].set_color('#101210')   

    def update_graph4():        
        ax4.clear()
        ax4.plot(x_data, y4_data, color="#ffeda3")
        ax4.set_ylim(0, 180)
        ax4.set_xlabel('Time [s]', color="white")
        ax4.set_ylabel('Oil Temperature [C]', color="white")
        ax4.tick_params(axis='x', colors='white')
        ax4.tick_params(axis='y', colors='white')
        ax4.spines['bottom'].set_color('white')  
        ax4.spines['left'].set_color('white') 
        ax4.spines['right'].set_color('#101210')   
        ax4.spines['top'].set_color('#101210')   

    def graph_handler(): 
        time.sleep(1)
        update_graph1()
        update_graph2()
        update_graph3()
        update_graph4()
        graf1.update()
        graf2.update()
        graf3.update()
        graf4.update()

    def handle_data():
        global x_data
        global y1_data, y2_data, y3_data, y4_data
        global previous_analysis_time
        global score
        global annoying
        
        if stop_bool == True: 
            
            # Check if it's time for real time analysis
            if time.time() - previous_analysis_time > 30:
                score_label.value = str(score[0])
                page.update()
                previous_analysis_time = time.time()
                t = threading.Thread(target=analyze.real_time_analyze, args=(y1_data, y2_data, y3_data, y4_data, annoying, score))
                t.start()
                
            
            temp = com_reader.get_data()
            
            for i in range(len(temp)):
                x_data.append(time.time() - start_time)  
                y1_data.append(temp[i][0])
                y2_data.append(temp[i][1]) 
                y3_data.append(temp[i][2]) 
                y4_data.append(temp[i][3]) 
                graph_handler()
        else:
            x_data = []
            y1_data, y2_data = [], []
            y4_data, y3_data = [], []
            graph_handler()

        
    def set_interval(func, sec):
        def func_wrapper():
            while True:
                func()
                time.sleep(1)
            
        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t
    
    previous_analysis_time = time.time()
    set_interval(handle_data, 1)

    def go_with_the_flow():
        #posl tolk kot je score coinov v wallet od userja
        print("sending reward " + score)
        #async with flow_client(
            #host=ctx.access_node_host, port=ctx.access_node_port
        #) as client:
            #block = await client.get_latest_block(is_sealed=False)
            

ft.app(target=main, route_url_strategy="path")
