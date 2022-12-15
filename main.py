import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

def animate_bar(results, interval=100):
    fig = plt.figure(figsize=(8,6))
    axes = fig.add_subplot(1,1,1)
    axes.set_ylim(0, 10)

    

    def update(frame):
        plt.clf()
        indices = [str(i) for i in results[frame]]
        plt.bar(indices, results[frame], color='blue')

    ani = FuncAnimation(fig, update, frames=range(len(results)), interval=interval, 
            repeat=False)
    plt.show()

