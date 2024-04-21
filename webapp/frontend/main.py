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

matplotlib.use("svg")
score = 100


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
    
    global start_time
    start_time = time.time()

    #page.theme_mode = ft.ThemeMode.SYSTEM
    page.bgcolor = "#101210"
    page.title = "rAId"
    page.scroll = "adaptive"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {
        
    }

    page.add(
        ft.Text("R", size=50, weight=ft.FontWeight.W_500, 
                spans=[ft.TextSpan("AI", ft.TextStyle(size=50, weight=ft.FontWeight.W_700, color="#3c8062")), ft.TextSpan("d", ft.TextStyle(size=50, weight=ft.FontWeight.W_500))]),
    )

    page.update()

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
            analysis(y1_data, y2_data, y3_data, y4_data)
            
            json_data = {
                "username": username,
                "x": x_data,
                "y1": y1_data,
                "y2": y2_data,
                "y3": y3_data,
                "y4": y4_data
            }
            AI_response = analyze.analyze(y1_data, y2_data, y3_data, y4_data)
            try:
                uri = "mongodb+srv://dragon:dragonhack123@dh.xbqmeva.mongodb.net/?retryWrites=true&w=majority&appName=DH"
                client = MongoClient(uri)
                db = client["dh"]
                collection = db["raid"]
                insert_result = collection.insert_one(json_data)
            except Exception as e:
                print("An error occurred:", e)
    
        else:
            stop_bool = True
            txt_stop="End & Save ride"
        
        # AI_response = analyze.analyze(y1_data, y2_data, y3_data, y4_data)
        
        button_stop.text = txt_stop
        button_stop.update()

    def login(e):
        global txt_login
        global username
        global button_login
        if username == "notloggendin":
            username = "TUKI PRIDE IME USERNAMA"
            txt_login = "Logout"
        else:
            username = "notloggendin"
            txt_login = "Login"
        print(txt_login)
        button_login.text = txt_login
        button_login.update()

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
    button_login = ft.ElevatedButton(text=txt_login, on_click=login)

    page.add(
        ft.Row([
            ft.Text("Click on this button to start analysis: ", size=20, weight=ft.FontWeight.W_500),
        ]),
        button_stop,
        button_login
    )


    page.update()

    def update_graph1():        
        ax1.clear()
        ax1.plot(x_data, y1_data, color="#a2faa2")
        ax1.set_ylim(0, 255)
        ax1.set_xlabel('Time [s]', color="white")
        ax1.set_ylabel('Hitrost [km / h]', color="white")
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
        
        if stop_bool == True: 
            
            # Check if it's time for real time analysis
            if time.time() - previous_analysis_time > 30:
                previous_analysis_time = time.time()
                AI_response = analyze.real_time_analyze(y1_data, y2_data, y3_data, y4_data)
                if score + AI_response > 0 and score + AI_response < 100:
                    score += AI_response
                print("Score: ", score)
            
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

    set_interval(handle_data, 1)
ft.app(target=main)
message.txt