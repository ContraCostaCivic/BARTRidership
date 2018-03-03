import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

sats = ['2017_1_Saturday.csv', '2018_1_Saturday.csv']
suns = ['2017_1_Sunday.csv', '2018_1_Sunday.csv']
weeks = ['2017_1_Weekday.csv', '2018_1_Weekday.csv']

def clean_value(text):
    text = str(text)
    text = text.replace('\t', '').replace(',', '').strip()
    if text == '-':
        text = '0'

    value = float(text)
    value = int(value)
    return value

def open_csv(filename):
    with open(filename) as f:
        data = pd.read_csv(f, index_col=0)

    data = data.iloc[0:47,0:47]
    data = data.applymap(clean_value)
    return data

sat_dfs = [open_csv(f) for f in sats]
sun_dfs = [open_csv(f) for f in suns]
week_dfs = [open_csv(f) for f in weeks]

#saturday 2017 vs 2018 comparison
jan17_sat_entry = sat_dfs[0].iloc[[-1]].transpose()
jan18_sat_entry = sat_dfs[1].iloc[[-1]].transpose()

sat_entry = jan17_sat_entry.copy()
sat_entry.columns = ['2017']
sat_entry['2018'] = jan18_sat_entry.divide(jan17_sat_entry)*100
sat_entry['2017'] = 100

#sunday 2017 vs 2018 comparison
jan17_sun_entry = sun_dfs[0].iloc[[-1]].transpose()
jan18_sun_entry = sun_dfs[1].iloc[[-1]].transpose()

sun_entry = jan17_sun_entry.copy()
sun_entry.columns = ['2017']
sun_entry['2018'] = jan18_sun_entry.divide(jan17_sun_entry)*100
sun_entry['2017'] = 100

#weekday 2017 vs 2018 comparison
jan17_week_entry = week_dfs[0].iloc[[-1]].transpose()
jan18_week_entry = week_dfs[1].iloc[[-1]].transpose()

week_entry = jan17_week_entry.copy()
week_entry.columns = ['2017']
week_entry['2018'] = jan18_week_entry.divide(jan17_week_entry)*100
week_entry['2017'] = 100

plt.plot(sat_entry.transpose())
plt.title('Saturday: Stations as entries')
plt.ylabel('Normalized Ridership (%)')
plt.ylim((50,120))
plt.xlabel('Year')
plt.savefig('saturday_2017v2018.png')

plt.plot(sun_entry.transpose())
plt.title('Sunday: Stations as entries')
plt.ylabel('Normalized Ridership (%)')
plt.ylim((50,120))
plt.xlabel('Year')
plt.savefig('sunday_2017v2018.png')

plt.plot(week_entry.transpose())
plt.title('Weekdays: Stations as entries')
plt.ylabel('Normalized Ridership (%)')
plt.ylim((50,120))
plt.xlabel('Year')
plt.savefig('weekdays_2017v2018.png')

#print(sat_dfs)
#print(sun_dfs)
#print(week_dfs)
