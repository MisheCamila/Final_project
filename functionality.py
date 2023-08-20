"""
Michelle Munoz
UPDATES and Funcitionality
"""
import csv
import json
import pandas as pd
import numpy as np
import matplotlib
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import matplotlib.animation as animation

#Read csv and j.son files
with open("AllStocks.json","r") as read_file:
    data_set=json.load(read_file)

data=[]    
with open("Lesson6_Data_Stocks.csv", 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
#Create a dictionary
stock_info = {}

for purchase_data in data:
    symbol = purchase_data["symbol"]
    shares = float(purchase_data["number_shares"])
    purchase_date = datetime.strptime(purchase_data["purchase_date"], "%m/%d/%Y")
#add date and close price withon dictionary
for stock in data_set:
        symbol = stock['Symbol']
        date = datetime.strptime(stock['Date'], "%d-%b-%y")
        close = stock['Close']
        if symbol not in stock_info:
            stock_info[symbol] = {'dates': [], 'value': []}
        
        stock_info[symbol]['dates'].append(date)
        stock_info[symbol]['value'].append(float(close))
# Multiply by number of shares if data is >= purchase date
stock_info[symbol]['value'] = [
    round(close * shares, 2) if date >= purchase_date else close
    for date, close in zip(stock_info[symbol]['dates'], stock_info[symbol]['value'])]
#Make grap with the average
symbols = list(stock_info.keys())
avg_values = [sum(values['value']) / len(values['value']) for values in stock_info.values()]
plt.figure(figsize=(10, 6))
plt.bar(symbols, avg_values, color='blue')
plt.xlabel('Stock Symbol')
plt.ylabel('Average Stock Value')
plt.title('Average Stock Value by Symbol')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.show()
# make a graph for each stock
plt.figure(figsize=(12, 6.75))
for symbols in stock_info:
    prices=stock_info[symbols]['value']
    dates=matplotlib.dates.date2num(stock_info[symbols]['dates'])
    name=symbols
    plt.plot(dates, prices, label=name)
    plt.xlabel('Date')
    plt.ylabel('Stock Value')
    plt.title('Stock Value Over Time')
    plt.legend()
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d %b %Y'))
    plt.savefig('line_chart.png')
    plt.show()
"""
ADD Funtionality using mplfinance and matplotlib.animation 
"""
#create a DataFrame
df = pd.DataFrame(data_set)
df['Date'] = pd.to_datetime(df['Date'])
#index as datime
df.set_index("Date", inplace=True)
#convert into a float
df['Low']=df.Low.replace('-',np.nan).astype(float)
df['Low'] = df['Low'].fillna(0)
df['Open']=df.Open.replace('-',np.nan).astype(float)
df['Open'] = df['Open'].fillna(0)
df['High']=df.High.replace('-',np.nan).astype(float)
#select specific stock F, FB,GOOGL,M,MSFT, RDS-A, IBM, AIG
aig_data = df.loc[df['Symbol'] == "AIG"]
#create animation
fig = mpf.figure(style='charles',figsize=(7,8))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(3,1,3)
def animate(ival):
    if (20+ival) > len(aig_data):
        ani.event_source.interval *= 3
        if ani.event_source.interval > 12000:
            exit()
        return
    data = aig_data.iloc[0:(20+ival)]
    ax1.clear()
    ax2.clear()
    mpf.plot(data,ax=ax1,volume=ax2,type='candle')

ani = animation.FuncAnimation(fig, animate, interval=250)
fig.suptitle('AIG plot', fontsize=14)
mpf.show()
#Create figure
mpf.plot(aig_data["2016-01-22":], figratio=(10, 6), type="candle", 
         mav=(21), volume=True,
         title = f"Price of AIG",
         tight_layout=True, style="binance", 
         savefig=f"AIG_stock.png")




