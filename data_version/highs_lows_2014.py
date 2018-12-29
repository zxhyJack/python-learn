import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data_version/sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(ValueError, 'miss date')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title('Daily high temperatures, July 2014', fontsize=24)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Tempereture(E)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
