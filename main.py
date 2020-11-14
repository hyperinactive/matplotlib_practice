from matplotlib import pyplot as plt

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

# -----------------------------------------
# gives a list of many available styles
# print(plt.style.available)

plt.style.use('seaborn')
# works like CSS
# we're overriding some of the style's params
# by using grid, linewidth, colors, etc...
# -----------------------------------------
# to make a plot we simply use.plot(x,y)
# plt.plot(ages_x, dev_y, label='All devs')
# k -> black; -- -> lines
# though this works, it's good to split arguments for better readability
# plt.plot(ages_x, dev_y, 'k--', label='All devs')
# -----------------------------------------
# format string
# fmt = '[marker][line][color]'
# optional
# there are various marker, line and color style in the docs
# -----------------------------------------
# the order in which the plots are being made matters
# they're being stacked in order of their creation

# py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# since we're suing the same age group, no need to have py_dev_x
# pass dev_x = ages_x now
# -----------------------------------------
py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000,
            71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708,
            108423, 101407, 112542, 122870, 120000]
# plt.plot(ages_x, py_dev_y, label='Python devs')
# b -> blue
# plt.plot(ages_x, py_dev_y, color='b', label='Python devs')
plt.plot(ages_x, py_dev_y, color='#5a7d9a', label='Python devs', linewidth=3)
# -----------------------------------------
js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674,
            68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660,
            99240, 108000, 105000, 104000]
plt.plot(ages_x, js_dev_y, color='#adad3b', label='Javascript', linewidth=3)
# -----------------------------------------
dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317,
         68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988,
         100000, 108923, 105000, 103117]
plt.plot(ages_x, dev_y, color='#444444', linestyle='--', label='All devs')
# -----------------------------------------
# adds a title to the plot
plt.title('Median salary by age (USD)')

# name the axis
plt.xlabel('Ages')
plt.ylabel('Median salary')

# -----------------------------------------
# 1st way of adding a legend
# pass a list containing the descriptions
# in the order in which the plots were added
# plt.legend(['All devs', 'Python devs'])

# but the more precise way is to add labels to the plots
# and just call it with no args
plt.legend()
# -----------------------------------------
# makes an underlying grid
plt.grid(True)
# -----------------------------------------
# tight_layout automatically adjusts subplot params so that the subplot(s) fits in to the figure area
# QOL change
plt.tight_layout()
# -----------------------------------------
# makes a copy of the figure and saves it in the root dir
# a path can be provided
# the figures can be saved through the GUI as well
plt.savefig('./plots/some_plot_name.png')
# -----------------------------------------
# pops a window containing our plot
plt.show()
