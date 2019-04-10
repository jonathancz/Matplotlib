# Part 16
'''
In this Matplotlib tutorial, we're going to cover how to create live updating 
graphs that can update their plots live as the data-source updates. You may want 
to use this for something like graphing live stock pricing data, or maybe you 
have a sensor connected to your computer, and you want to display the live sensor 
data. To do this, we use the animation functionality with Matplotlib.
'''

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style # To make it more appealing

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('example.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()