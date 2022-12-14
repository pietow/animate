import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

def anmimate_bar(values, func):
    fig = plt.figure(figsize=(8,6))
    axes = fig.add_subplot(1,1,1)
    axes.set_ylim(0, 10)

    indices = list(range(0, 10))
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


    def update(frame):
        plt.clf()
        func(values)
        print(values)
        plt.bar(indices, values, color='blue')

    ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128))
    plt.show()

