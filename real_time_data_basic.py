# Plotting real time data
import random
# count
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt

# to animate charts, import FuncAnimation from the matplotlib
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')
x_vals = []
y_vals = []

# function count from the itertools just counts up 1 number at the time
# next(index) will be provided with the next value to be counted by the count() function
index = count()


def animate(i):
    # for each tick append a coordinate to the axes
    # x appends integers - y append a random number between 0 and 5
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))

    # to prevent plots stacking on top on each other, we clear the old one before making new plots
    plt.cla()
    # make a plot with the current set of values
    plt.plot(x_vals, y_vals)


# 1st param, a figure to animate
# 2nd param, a function to describe the animation
# 3rd param, an interval in which to call the anim fuction, in ms
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()

