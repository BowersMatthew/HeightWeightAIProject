import matplotlib.pyplot as plt
from src.Data.Person import Person

def coolgraph(people, weights, train):

    """
    :param people list of the data points:
    :param weights holds all the weights:
    :param train holds the best weights and error:
    :return displays the graph :
    """
    maleheight = []
    maleweight = []
    femaleheight = []
    femaleweight = []
    #adds heights and weights for both genders into a list
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
    #add dots to scatter plot
    for data, color, group in zip(data, colors, groups):
        x, y = data
        ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=10, label=group)
    #title
    plt.title('Graph of ' + train.kind + " " + str(train.params[len(train.params) - 2]))
    #creating the best line
    z = determineline(weights)
    ax.plot(z[0], z[1], 'b--')
    ax.set_xlabel('Height')
    ax.set_ylabel('Weight')
    terr = ""
    if train.kind == 'Hard':
        terr = str(train.harderror)
    else:
        terr = "{:.2f}".format(train.softerror)
    #Adding labels
    ax.text(.6, .05, 'Total Error = ' + str(terr), bbox={'facecolor': 'blue', 'alpha': 0.5, 'pad': 3})
    ax.text(.6, .11, 'Neuron ' + lineasstring(z), bbox={'facecolor': 'yellow', 'alpha': 0.5, 'pad': 3})
    plt.axis([0, 1, 0, 1])
    plt.legend(loc=2)
    plt.show()
def determineline(weights):
    #solve for x and y intercept then use those to graph
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

#returns equation of the line as a string
def lineasstring(z):
    x = z[0][0]
    y = z[1][1]
    output = "{:.2f}".format(x) + " x"
    if z[1][1] > 0:
        output += "+"
    output += "{:.2f}".format(y) + " y = 0"
    return output



