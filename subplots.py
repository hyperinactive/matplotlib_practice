import pandas as pd
from matplotlib import pyplot as plt

# notice that an instance of plt object was never created
# pyplot was imported and it has a state: to work with a main figure
# figure is the container that holds the plots
# axes are the actual plots
# just as we can have multiple plots we can have multiple figures

# plt.gcf()
# plt.gca()
# a more OOP approach would be to use the subplots method though

plt.style.use('seaborn')

data = pd.read_csv('data_set_7.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# instantiate a figure and axes(plots)
# unless specified axes will default to a 1 x 1 row/column
# fig, ax = plt.subplots()
# nrows ncolums to specify the number of rows and column
# since we'll be getting 2 axes we will place them into ax1 anx ax2
# note: a single axis can have a list of multiple axes returned

# sharex = True -> makes the x axis ticks only once and the plots will share it
# same stuff for sharey
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

# so whenever we use plt -> use ax
# and xlabel, ylabel become set_xlable, set_ylabel

# each axis can have different legends, titles etc..
ax1.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Median Salary (USD)')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()
