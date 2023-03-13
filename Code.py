import matplotlib.pyplot as plt

# define the disease names and scores
x = ['Disease A', 'Disease B', 'Disease C']
y = [7.2, 4.5, 9.3]
y_err = [1.2, 1.5, 1.8]
labels = ['b', 'c', 'a']
colors = ['red', 'green', 'blue']
# create a bar chart
plt.bar(x, y, color=colors)

# set the chart title and axis labels
plt.title('Disease Severity Scores', fontsize=20)
plt.xlabel('Disease', fontsize=20)
plt.ylabel('Score', fontsize=20)
plt.yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# plot the data with error bars
plt.errorbar(x, y, yerr=y_err, fmt='o', capsize=4)

for i, v in enumerate(y):

    plt.text(i, v + -0.5 * y[i], labels[i], ha='center', fontsize=20)

# display the chart
plt.show()
