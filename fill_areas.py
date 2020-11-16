# FILLS

# fills can be used to mark some patterns or pieces of the plot
# e.g. conditional fills to mark where the plot dips under a certain line
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data_set_2.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')
plt.plot(ages, py_salaries, label='Python')

# median of all dev salaries
overall_median = 57287

# fill between fill the part between provided axis, plots
# one arg -> fills from the plot to the bottom
# alpha=value -> optional parameter, makes the fill transparent
# by passing a line, the parts beneath the line are filled up and the parts above filled down to it
# plt.fill_between(ages, py_salaries, overall_median, alpha=0.4)
# ------------------------------------------------
# we can add a condition too where=
# this will fill all python wages above the line
# interpolate prevents clipping
# plt.fill_between(ages, py_salaries, overall_median, where=(py_salaries > overall_median), interpolate=True, alpha=0.4)

# fill from the line to the bottom
# plt.fill_between(ages, py_salaries, overall_median, where=(py_salaries <= overall_median),
# interpolate=True, alpha=0.4)
# ------------------------------------------------

# the very same can be done for 2 plots
plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries > dev_salaries), interpolate=True, alpha=0.4,
                 label='Above average')
plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries <= dev_salaries), interpolate=True, alpha=0.4,
                 label='Below average')

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()
