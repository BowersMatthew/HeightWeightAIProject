import matplotlib.pyplot as plt
from src.Data.Person import Person

def errorgraph(data):
    error = data.errors
    x = list(range(0, len(data.errors)))
    plt.scatter(x, error, alpha=0.8, edgecolors='none', s=10)
    plt.axis([0, 1000, 0, max(error) + max(error)/10])
    plt.show()