import numpy as np
import matplotlib.pyplot as plt
from src.Data.Person import Person

def coolgraph(people):
    maleheight = []
    maleweight = []
    femaleheight = []
    femaleweight = []
    for p in people:
        if p.sex == Person.MALE:
            maleheight.append(p.height)
            maleweight.append(p.weight)
        else:
            femaleheight.append(p.height)
            femaleweight.append(p.weight)

    male = (maleheight, maleweight)
    female = (femaleheight, femaleweight)

    data = (male, female)
    colors = ("red", "green")
    groups = ("male", "female")

    # Create plot
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, facecolor="1.0")

    for data, color, group in zip(data, colors, groups):
        x, y = data
        ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=10, label=group)

    plt.title('Graph of Data')
    plt.legend(loc=2)
    plt.show()