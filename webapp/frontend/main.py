import flet as ft
import time
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from flet.matplotlib_chart import MatplotlibChart
import com_reader
matplotlib.use("svg")


def main(page: ft.Page):

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


    def generate_data():
        return np.random.rand()

    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    fig3, ax3 = plt.subplots()
    fig4, ax4 = plt.subplots()
    x1_data, y1_data = [], []
    x2_data, y2_data = [], []
    x3_data, y3_data = [], []
    x4_data, y4_data = [], []
    temp = [[]]

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


    page.add(
        ft.Row([
            ft.Text("Click on this button to start analysis: ", size=20, weight=ft.FontWeight.W_500),
        ])
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
        ax2.set_ylabel('Poraba')

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
        for i in range(len(temp)):
            x1_data.append(time.time() - start_time)  
            y1_data.append(temp[i][0])
            x2_data.append(time.time() - start_time)  
            y2_data.append(temp[i][1]) 
            x3_data.append(time.time() - start_time)  
            y3_data.append(temp[i][2]) 
            x4_data.append(time.time() - start_time)  
            y4_data.append(temp[i][3]) 

    while True:
        time.sleep(1)
        #temp = com_reader.get_data()
        temp = com_reader.fake_data()
        handle_data()
        graph_handler()
        

    print("Ona mene pali")
    
    

ft.app(target=main)