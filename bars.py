# Bar Charts
from matplotlib import pyplot as plt
import numpy as np

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# MULTIPLE BARS
# just stacking bars won't work
# we need to import numpy
# numpy array
# x_indexes will be numbered versions of x values
x_indexes = np.arange(len(ages_x))  # 0 1 2 3 4 5 6 7 8 9 10 -> because we have 11 elements in ages_x

# now, instead of passing ages_x, we pass the numpy array
# the bars will still be stacked on top of each other, but now we can shift the bars around and see the data better

bar_width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.style.use('fivethirtyeight')
# .bar will give us a bar
# specify the width of our bars
# now we add/subtract the width
plt.bar(x_indexes - bar_width, dev_y, width=bar_width, color='#5a7d9a', label='All devs', linewidth=3)
# ----------------------------------------- # we can mix and match some plots
plt.bar(x_indexes, py_dev_y, width=bar_width, color='#444444', linestyle='--', label='Python')
# -----------------------------------------
plt.bar(x_indexes + bar_width, js_dev_y, width=bar_width, label='Javascript')
# -----------------------------------------
plt.title('Median salary by age (USD)')

plt.xlabel('Ages')
plt.ylabel('Median salary')
plt.legend()

# because we made our plot with a numpy array we need to set the x ticks back to
# our original age groups
plt.xticks(ticks=x_indexes, labels=ages_x)

plt.tight_layout()
plt.show()
