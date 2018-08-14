# path = 'f:\\Python_test\\BasicKnowledge\\google_stock_data.csv'
'''
file = open(path)

for line in file:
    print(line)
'''

'''
lines = [line.strip().split(',') for line in open(path)]
print(lines[0])
'''

import csv
from datetime import datetime

path = 'f:\\Python_test\\BasicKnowledge\\google_stock_data.csv'
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)  # The first line is the header
'''
data = [row for row in reader]  # Read the remaining(剩余) data

print(header)
print(data[0])
'''

data = []
for row in reader:
    # row = [Date,     Open, High, Low, Close, Volume, Adj.Close]
    # row = [datetime, float,float,float,float, integer,float]
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])  # 价格
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high, low, volume, adj_close])

# Compute and store daily stock returns

return_path = 'f:\\Python_test\\BasicKnowledge\\google_returns.csv'
file = open(return_path, 'w')
writer = csv.writer(file)
writer.writerow(['Date', 'Returns'])

for i in range(len(data) - 1):
    today_row = data[i]
    today_date = today_row[0]
    today_price = today_row[-1]
    yesterdays_row = data[i + 1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (today_price - yesterdays_price) / yesterdays_price
    formatted_date = today_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])
