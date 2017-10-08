import numpy as np
import matplotlib.pyplot as plt
from src.Data.Person import Person

def coolgraph(people, weights, train):
    '''
    Weights is a 2d list of 3 seperate weights
    Find out how to turn those into a line
    and plot the lines
    '''
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

    plt.title('Graph of ' + train.kind)
    z = determineline(weights)
    ax.plot(z[0],z[1], 'b--')
    ax.set_xlabel('Height')
    ax.set_ylabel('Weight')
    terr = ""
    if train.kind == 'hard':
        terr = str(train.harderror)
    else:
        #{:.2f}".format(f)
        terr = "{:.2f}".format(train.softerror)
    ax.text(.6, .05, 'Total Error = ' + str(terr), bbox={'facecolor': 'blue', 'alpha': 0.5, 'pad': 3})
    plt.axis([0, 1, 0, 1])
    plt.legend(loc=2)
    plt.show()
def determineline(weights):
    #solve for x and y intercept then use those to graph
    #print(weights)
    x = []
    y = []
    y.append(0)
    yint = -weights[2]/weights[1]
    y.append(yint)
    xint = -weights[2]/weights[0]
    x.append(xint)
    x.append(0)
    z = []
    z.append(x)
    z.append(y)
    return z




