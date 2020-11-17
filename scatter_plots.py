# Scatter plots
# use to check if there is any correlation in the data

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')
#
# x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
# y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

# custom colors can be added to the plot
# colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]

# s= size scales the size of the plots
# marker='x'
# cmap will chagne our colors based on what we passed at c

# can make custom size as well
# sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
#          538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

# cbar servers like a legend showing the gradient of the data presented
# cbar = plt.colorbar()
# cbar.set_label('Some level')

data = pd.read_csv('data_set_4.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

# plt.scatter(x, y, s=sizes, c=colors, cmap='Greens', edgecolors='black', linewidths=1, alpha=0.75)

# clever stuff, the ratio between likes and dislikes can help us in reading the data better
# can use the ratio to color map the plot
plt.scatter(view_count, likes, edgecolors='black', linewidths=1, alpha=0.75, c=ratio, cmap='summer')

cbar = plt.colorbar()
cbar.set_label('Like to dislike ratio')

# same as before, the plot can be scaled by log
# some outlier skewing the data?
# log scale it!
plt.xscale('log')
plt.yscale('log')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()
