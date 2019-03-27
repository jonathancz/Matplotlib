import matplotlib.pyplot as plt
import csv

# Part 7
'''
Many times, people want to graph data from a file. There are many types of files, 
and many ways you may extract data from a file to graph it. Here, we'll show a 
couple of ways one might do this. First, we'll use the built-in csv module to 
load CSV files, then we'll show how to utilize NumPy, which is a third-party module, 
to load files.
'''
x = []
y = []

with open('example.txt', 'r') as csvfile:
	plots = csv.reader(csvfile, delimiter = ',')
	for row in plots:
		x.append(int(row[0]))
		y.append(int(row[1]))

plt.plot(x,y, label='loaded from file.')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()