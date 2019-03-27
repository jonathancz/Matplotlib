import matplotlib.pyplot as plt

# Part 5
'''
In this Matplotlib data visualization tutorial, 
we cover how to create stack plots. The idea of
 stack plots is to show "parts to the whole" over 
 time. A stack plot is basically like a pie-chart, 
 only over time.

Let's consider a situation where we have 24 hours 
in a day, and we'd like to see how we're spending 
out time. 
We'll divide our activities into: 
Sleeping, eating, working, and playing.
'''
days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7] # hours
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

plt.plot([], [], color = 'm', label = 'Sleeping', linewidth = 5)
plt.plot([], [], color = 'c', label = 'Eating', linewidth = 5)
plt.plot([], [], color = 'r', label = 'Working', linewidth = 5)
plt.plot([], [], color = 'k', label = 'Playing', linewidth = 5)


plt.stackplot(days, sleeping, eating, working, playing, colors = ['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()