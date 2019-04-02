import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates


# Part 10
'''
In this Matplotlib tutorial, we're going to be talking about some 
of the possible customizations to graphs. In order to start modifying 
the subplots, we have to define them. We will talk about them soon, 
but there are two major ways to define subplots, and to structure them. 
For now, we'll just use one of them, but we will be explaining them shortly.
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
                                                          unpack=True,
                                                          # %Y = full year. 2015
                                                          # %y = partial year 15
                                                          # %m = number month
                                                          # %d = number day
                                                          # %H = hours
                                                          # %M = minutes
                                                          # %S = seconds
                                                          # 12-06-2014
                                                          # %m-%d-%Y
                                                          converters={0: bytespdates2num('%Y-%m-%d')})
    



    
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