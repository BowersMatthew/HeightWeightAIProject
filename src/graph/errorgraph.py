import matplotlib.pyplot as plt

#displays error graph
def errorgraph(data):
    error = data.errors
    x = list(range(0, len(data.errors)))
    plt.scatter(x, error, alpha=0.8, edgecolors='none', s=5)
    plt.title('Graph of error for ' + data.kind + " " + str(data.params[len(data.params) - 2]))
    plt.axis([0, 1000, 0, max(error) + max(error)/10])
    plt.show()