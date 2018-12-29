import csv
from matplotlib import pyplot as plt
from datetime import datetime

first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
print(first_date)

filename = 'data_version/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    highs = []
    dates = []
    for row in reader:
        dates.append(datetime.strptime(row[0], '%Y-%m-%d'))
        highs.append(int(row[1]))
    print(dates)
    print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# 设置图形的格式
plt.title('Daily high temperatures, July 2014', fontsize=24)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Tempereture(E)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
