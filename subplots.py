# Part 19
'''
In this Matplotlib tutorial, we're going to be discussion subplots. There are two major ways 
to handle for subplots, which are used to create multiple charts on the same figure. For now, 
we'll start with a clean slate of code. If you're following along linearly, then make sure to 
keep the old code on hand, or you can always revisit the previous tutorial for the code again.
'''
import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()

def create_plots():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        ys.append(y)
    return xs, ys
ax1 = fig.add_subplot(221) # first number is the height, second the width, third the plot
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)


x,y = create_plots()
ax1.plot(x,y)

x,y = create_plots()
ax2.plot(x,y)

x,y = create_plots()
ax3.plot(x,y)

plt.show()