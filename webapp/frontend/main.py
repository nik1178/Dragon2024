import flet
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def main(page: flet.Page):
    def generate_data():
        return np.random.rand()

    def update_plot(frame):
        x_data.append(time.time() - start_time)  
        y_data.append(generate_data())           
        ax.clear()
        ax.plot(x_data, y_data)
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Poraba')

    fig, ax = plt.subplots()
    x_data, y_data = [], []

    start_time = time.time()

    ani = animation.FuncAnimation(fig, update_plot, interval=1000)

    plt.show()

flet.app(target=main)