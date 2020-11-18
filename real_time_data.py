# Plotting real time data - "real world example"
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')
index = count()


def animate(i):
    data = pd.read_csv('data_set_6.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
    # clear axes
    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    # because cla clears legends too, must generate a new one each time
    plt.legend(loc='upper left')
    plt.tight_layout()


# 1st param, a figure to animate
# 2nd param, a function to describe the animation
# 3rd param, an interval in which to call the anim fuction, in ms
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
