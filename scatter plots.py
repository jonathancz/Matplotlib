import matplotlib.pyplot as plt

# Part 4
'''
Next up, we cover scatter plots! The idea of scatter 
plots is usually to compare two variables, or three 
if you are plotting in 3 dimensions, looking for 
correlation or groups.
'''
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]

plt.scatter(x, y, label = 'skitscat', color = 'k', s = 300, marker="*")


plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()