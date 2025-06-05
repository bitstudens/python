import csv
import matplotlib.pyplot as plt
import numpy as np

data = []
with open('data.csv', newline='',  encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)


def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return 0
        
coutries =  [row['Country/Region'] for row in data]       
confirmed =  [row['Confirmed'] for row in data] 
deaths =  [safe_convert(row['Deaths']) for row in data]
recovered =  [row['Recovered'] for row in data]
recovered_per_100 =  [safe_convert(row['Recovered / 100 Cases']) for row in data]
deaths_per_100 =  [safe_convert(row['Deaths / 100 Cases']) for row in data]  
week_change =  [safe_convert(row['1 week change']) for row in data]  


top10_confirmed = sorted(zip(coutries, confirmed), key=lambda x: safe_convert(x[1]), reverse=True)[:10]
x,y = zip(*top10_confirmed)
plt.figure(figsize=(10, 6))
plt.barh(x, [safe_convert(i) for i in y], color='blue')
plt.xlabel('Confirmed Cases')
plt.title('Top 10 Countries by Confirmed COVID-19 Cases')
plt.gca().invert_yaxis()
plt.show()

top10deaths = sorted(zip(coutries, deaths), key=lambda x: safe_convert(x[1]), reverse=True)[:10]
x, y = zip(*top10deaths)
plt.figure(figsize=(10, 6))
plt.barh(x, [safe_convert(i) for i in y], color='red')
plt.xlabel('Deaths')
plt.title('Top 10 Countries by COVID-19 Deaths')
plt.gca().invert_yaxis()
plt.show()

confirmed_numeric = [safe_convert(i[1]) for i in top10_confirmed]
deaths_numeric = [safe_convert(i[1]) for i in top10deaths]
contries_numeric = [i[0] for i in top10_confirmed]

plt.figure(figsize=(10, 6))
plt.scatter(confirmed_numeric, deaths_numeric, alpha=0.7)
plt.xlabel('Confirmed Cases')
plt.ylabel('Deaths')
plt.title('Confirmed Cases vs Deaths for Top 10 Countries')
plt.grid(True)
plt.show()
