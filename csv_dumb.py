# CSV - general way of loading data - not the fastest way - numpy better lol
import csv
from matplotlib import pyplot as plt
from collections import Counter
import numpy as np

plt.style.use('seaborn')
# -----------------------------------------
# CVS rows are separated by ,
# CVS data (columns) is separated by ;
# row_id, languages
# e.g.
# 1, HTML; python; java
# -----------------------------------------
# there are many ways of extracting data from CVS
# cvs module
# read csv from pandas
# load txt from numpy
# -----------------------------------------
# csv module

with open('data_set_1.csv') as csv_file:
    # dict reader will make dictionaries
    # we can access the data by key
    # e.g. for the first entry
    # {'Responder_id': '1', 'LanguagesWorkedWith': 'HTML/CSS;Java;JavaScript;Python'}
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()
    # row = next(csv_reader)
    # print(row)
    # print(row['LanguagesWorkedWith'].split(';'))

    # .update() well, updates the counter
    # loop over the rows of csv and keep track of all languages that appear
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []

# most common will return the most common items from the counter
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

# we parsed the data, and now we have what we need to make our plots
# print(languages)
# print(popularity)
# barh -> horizontal bar
languages.reverse()
popularity.reverse()
plt.barh(languages, popularity)
# -----------------------------------------
plt.title('Most popular languages')
plt.ylabel('Programing languages')
# plt.xlabel('Number of devs')
# plt.legend()
plt.tight_layout()
plt.show()
