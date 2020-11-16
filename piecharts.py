from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# slices = [60, 40, 20, 20]
# labels = ['First', 'Second', 'Third', 'Fourth']
# colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

# tip: don't use pie charts if you're comparing more than 6 items
slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript',
          'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']

# to emphasis a certain slice we can provide an explode argument that will offset
explode = [0, 0, 0, 0.1, 0]

# shadow=True, adds a shadow to the chart making it more 3d
# startangle=90 rotates the pie chart

# adding % to the charts
# autopct='%1.1f%%'

# pass the slices and their names
# additional stuff, can thicken the wedge -> expects a dictionary
# for more customizations see the docs
# plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})
plt.pie(slices[0:5], explode=explode, labels=labels[0:5], startangle=120, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

plt.title('My not so awesome pie chart')
plt.tight_layout()
plt.show()
