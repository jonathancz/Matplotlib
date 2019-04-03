

import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates
import datetime as dt

#Part 11
'''
n this Matplotlib tutorial video, we're going to cover how to handle the 
conversion of unix time stamps to then plot date stamps in your graph. 
With the Yahoo Finance API, you will notice that if you use large time frames, 
like 1y for one year, you will get those date stamps we've been working with, but, 
if you use something like 10d for 10 days, you will instead get timestamps that 
are unix time.

Unix time is the number of seconds after Jan 1st 1970, and it represents a normalized 
method for time across programs. That said, Matplotlib doesn't want unix time stamps. 
'''

def bytespdates2num(fmt, encoding = 'utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b): 
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter



def graph_data(stock):    

    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0)) #subplots


    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line:
                stock_data.append(line)


    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True)

    dateconv = np.vectorize(dt.datetie.fromtimestamp)
    date = dateconv(date)

    #date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
    #                                                      delimiter=',',
    #                                                      unpack=True,
    #                                                      converters={0: bytespdates2num('%Y-%m-%d')})



    
    ax1.plot_date(date, closep)
    
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1.grid(True) #, color = 'g', linestyle = '-')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.subplots_adjust(left = 0.09, bottom = 0.20, right = 0.94, top = 0.90, wspace = 0.2, hspace = 0)
    plt.show()

graph_data('AAPL')