# HISTOGRAMS
# used when bar charts have too many things to track
# it will group stuff into similar piles (bins)
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# -----------------------------------------
# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
# -----------------------------------------

# bins=number -> number of groups to sort data into
# plt.hist(ages, bins=5, edgecolor='black')

# usually best if the bins are made by us -> more accurate
# bins = [10, 20, 30, 40, 50, 60]


data = pd.read_csv('data_set_3.cvs')
ids = data['Responder_id']
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# log=True
# plots on a logarithmic scale
# if some values are waaay bigger than others me may want to scale things down
plt.hist(ages, bins=bins, edgecolor='black', log=True)

median_age = 29
color = '#fc4f30'

# axis vertical line
# adds a vertical line onto the histogram
plt.axvline(median_age, color=color, label='Age median')

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()
