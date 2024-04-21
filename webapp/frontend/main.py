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

matplotlib.use("svg")


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
    global x1_data, x2_data, x3_data, x4_data
    global y1_data, y2_data, y3_data, y4_data
    
    global previous_analysis_time
    

    page.theme_mode = ft.ThemeMode.SYSTEM
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
        global x1_data, x2_data, x3_data, x4_data
        global y1_data, y2_data, y3_data, y4_data
        global username
        
        if stop_bool:
            stop_bool = False
            txt_stop="Start ride"
            
            json_data = {
                "username": username,
                "x1": x1_data,
                "x2": x2_data,
                "x3": x3_data,
                "x4": x4_data,
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
    x1_data, y1_data = [], []
    x2_data, y2_data = [], []
    x3_data, y3_data = [], []
    x4_data, y4_data = [], []

    start_time = time.time()

    
    graf1 = MatplotlibChart(fig1, isolated=True, expand=True)
    graf2 = MatplotlibChart(fig2, isolated=True, expand=True)
    graf3 = MatplotlibChart(fig3, isolated=True, expand=True)
    graf4 = MatplotlibChart(fig4, isolated=True, expand=True)
    
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
        button_login,
    )


    page.update()

    def update_graph1():        
        ax1.clear()
        ax1.plot(x1_data, y1_data)
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Poraba')

    def update_graph2():          
        ax2.clear()
        ax2.plot(x2_data, y2_data)
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Obrati')

    def update_graph3():           
        ax3.clear()
        ax3.plot(x3_data, y3_data)
        ax3.set_xlabel('Time (s)')
        ax3.set_ylabel('Poraba')

    def update_graph4():        
        ax4.clear()
        ax4.plot(x4_data, y4_data)
        ax4.set_xlabel('Time (s)')
        ax4.set_ylabel('Poraba')

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
        global x1_data, x2_data, x3_data, x4_data
        global y1_data, y2_data, y3_data, y4_data
        global previous_analysis_time
        
        if stop_bool == True: 
            
            # Check if it's time for real time analysis
            if time.time() - previous_analysis_time > 30:
                previous_analysis_time = time.time()
                AI_response = analyze.real_time_analyze(y1_data, y2_data, y3_data, y4_data)
            
            temp = com_reader.get_data()
            for i in range(len(temp)):
                x1_data.append(time.time() - start_time)  
                y1_data.append(temp[i][0])
                x2_data.append(time.time() - start_time)  
                y2_data.append(temp[i][1]) 
                x3_data.append(time.time() - start_time)  
                y3_data.append(temp[i][2]) 
                x4_data.append(time.time() - start_time)  
                y4_data.append(temp[i][3]) 
                graph_handler()
        else:
            x1_data, y1_data = [], []
            x2_data, y2_data = [], []
            x3_data, y3_data = [], []
            x4_data, y4_data = [], []
            graph_handler()
        
   
    def set_interval(func, sec):
        def func_wrapper():
            set_interval(func, sec)
            func()
        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t
    
    previous_analysis_time = time.time()
    set_interval(handle_data, 1)

ft.app(target=main)