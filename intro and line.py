import matplotlib.pyplot as plt

# Part 1 =====================================
#plt.plot([1,2,3], [5,7,4])
#plt.show()

# Part 2 =====================================
'''
we're going to cover legends, titles, 
and labels within Matplotlib. A lot of times, 
graphs can be self-explanatory, but having a 
title to the graph, labels on the axis, and 
a legend that explains what each line is can 
be necessary.
'''

'''
x = [1, 2, 3]
y = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 14, 12]


plt.plot(x,y, label = 'First Line')
plt.plot(x2, y2, label = 'Second Line')

plt.xlabel('Plot Number')
plt.ylabel('Important Var')

plt.title('Interesting Graph\nCheck it out') # \n for subtitle
plt.legend()
plt.show()

'''

# Part 3 =====================================
'''
The plt.bar creates the bar chart for us. If you do not 
explicitly choose a color, then, despite doing multiple 
plots, all bars will look the same. This gives us a change 
to cover a new Matplotlib customization option, however. 
You can use color to color just about any kind of plot, 
using colors like g for green, b for blue, r for red, and 
so on. You can also use hex color codes, like #191970

Next, we can cover histograms. Very much like a bar chart, 
histograms tend to show distribution by grouping segments together.
Examples of this might be age groups, or scores on a test. 
Rather than showing every single age a group might be, maybe 
you just show people from 20-25, 25-30... and so on. 
'''
#x = [2, 4, 6, 8, 10]
#y = [6, 7, 8, 2, 4]

#x2 = [1, 3, 5, 9, 11]
#y2 = [7, 8, 2, 4, 2]

population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 120, 121, 122, 130, 111, 115, 112, 80, 75, 65, 54, 44, 43, 42, 48]

#ids = [x for x in range(len(population_ages))] # creates a list with 1, 2, 3, 4.... so on.

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
plt.hist(population_ages, bins, histtype='bar', rwidth = 0.8)


#plt.bar(x, y, label = 'Bars 1', color = '#2ecc71') # Bar charts
#plt.bar(x2, y2, label = 'Bars 2', color = '#9b59b6')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
