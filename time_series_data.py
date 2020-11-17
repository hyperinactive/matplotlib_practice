# TIME SERIES DATA
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt

# importing dates from matplotlib
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

# list of dates, created with the pythons date module
# dates = [
#     datetime(2019, 5, 24),
#     datetime(2019, 5, 25),
#     datetime(2019, 5, 26),
#     datetime(2019, 5, 27),
#     datetime(2019, 5, 28),
#     datetime(2019, 5, 29),
#     datetime(2019, 5, 30)
# ]
#
# y = [0, 1, 3, 4, 6, 5, 7]
# -------------------------------------------------------------------
# plt.plot_date(dates, y, linestyle='solid')
#
# # so far, all work's been done on the plots themselves, but not the figure
# # to get the figure:
# # gcf = GET CURRENT FIGURE
# # autofmt_xdate() will format the figure
# plt.gcf().autofmt_xdate()
#
# # can format the date to our liking
# date_format = mpl_dates.DateFormatter('%d, %b %Y')
# # to set the format onto our figure, we need to "grab it"
# # gca - get current axis.xaxis X axis
# plt.gca().xaxis.set_major_formatter(date_format)
# -------------------------------------------------------------------

data = pd.read_csv('data_set_5.csv')
# because the data is being read as string, we'll we encountering some problems
# the solution is to parse the data to dates
# we can do that with a pandas method to_datetime
data['Date'] = pd.to_datetime(data['Date'])
# sort the dates
# inplace will mutate the data, normally we'd have to type data = data.sort_values('Date')
# sort_values('Date') -> sort only the "Date" column
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')
plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()
