import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.pyplot as plt

path = 'seattle_weather_1948-2017.csv'
sea_w = pd.read_csv(path).head(100)

fig, ax = plt.subplots()

ax.plot(sea_w['DATE'], sea_w['PRCP'], marker = None, color = 'r', linestyle="-")
ax.xaxis.set_major_locator(MaxNLocator(nbins=10))

plt.xticks(rotation=25)
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter(('%Y-%m')))

ax.set_xlabel("Date (YYYY/MM)")
ax.set_ylabel("Precipitation")
ax.set_title("Seattle Forecast Analysis")

plt.show()
