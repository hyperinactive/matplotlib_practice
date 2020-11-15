import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('seaborn')
# with pandas . read_cvs we can read the csv files
# creates a dictionary - no need to loop
data = pd.read_csv('data.cvs')
row_id = data['Responder_id']
languages = data['LanguagesWorkedWith']

language_counter = Counter()

for item in languages:
    language_counter.update(item.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()
plt.barh(languages, popularity)
# -----------------------------------------
plt.title('Most popular languages')
plt.ylabel('Programing languages')
plt.tight_layout()
plt.show()
