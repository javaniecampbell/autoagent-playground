# filename: get_ytd_stock_price.py

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# get data on NVDA and TSLA
nvda = yf.download('NVDA', start=pd.to_datetime('today').strftime('%Y-01-01'), end=pd.to_datetime('today').strftime('%Y-%m-%d'))
tsla = yf.download('TSLA', start=pd.to_datetime('today').strftime('%Y-01-01'), end=pd.to_datetime('today').strftime('%Y-%m-%d'))

# calculate the percentage change
nvda['Percent Change'] = nvda['Adj Close'].pct_change()
tsla['Percent Change'] = tsla['Adj Close'].pct_change()

# Plotting the graph
plt.plot(nvda.index, nvda['Percent Change'].cumsum(), label='NVDA')
plt.plot(tsla.index, tsla['Percent Change'].cumsum(), label='TSLA')

plt.legend(loc='best')
plt.grid(True)

# Provide the title and labels for the plot.
plt.title('NVDA vs. TSLA Stock Price Change YTD')
plt.xlabel('Date')
plt.ylabel('Percentage Change')

# Show the plot and save it
plt.savefig('nvda_vs_tsla_ytd.png')
plt.show()