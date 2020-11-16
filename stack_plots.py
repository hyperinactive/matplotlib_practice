# Stack plots
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# points scored at every minute
# player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
# player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
# player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

# can also just pass every single arg, but this is cleaner
players = [player1, player2, player3]
labels = ['player1', 'player2', 'player3']

colors = ['#008fd5', '#e5ae37', '#6d904f']

plt.stackplot(minutes, players, labels=labels, colors=colors)

# by default the legend appears in the upper left
# to change the location, use loc=
# plt.legend(loc='upper left')
# strings work, but if we need to be more precise, use loc=(some_coordinates)
plt.legend(loc=(0.07, 0.05))
plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Yellow = #e5ae37
# Green = #6d904f
