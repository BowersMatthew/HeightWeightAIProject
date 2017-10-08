from src.Data.Person import Person
from math import exp


class Train:

    def __init__(self, people, params):
        self.params = params
        self.iterations = 0
        self.errors = []
        self.besterr = 100000
        self.bestw = []
        self.data = []
        self.test = []
        if len(params) == 6:
            self.kind = 'Hard'
            self.weights = Train.hard(self, people, params)
        elif len(params) == 7:
            self.kind = 'Soft'
            self.weights = Train.soft(self, people, params)
        else:
            print("Invalid number of params")

    # params order should be [starting weights, alpha, max iterations, desired error, cut, num people]
    def hard(self, people, params):
        self.dividedata(people, params[4], params[5])
        #start best weights as original weights
        w = params[0]
        self.bestw = w
        weights = [w]
        for i in range(0, params[2]):
            for p in self.data:
                #get predicted values
                p.pred = Train.cnet(w, p, 'hard')
                #begin training
                w = Train.trainw(w, p, params[1])
            weights.append(w)
            if self.addterr(self.calcharderror(w, self.test), w) < params[3]:
                break
        return weights

    # params order should be [starting weights, alpha, gain, max iterations, desired error, cut, num people]
    def soft(self, people, params):
        self.dividedata(people, params[5], params[6])
        w = params[0]
        self.bestw = w
        weights = [w]

        for i in range(0, params[3]):
            for p in self.data:
                p.pred = Train.fbip(params[2], Train.cnet(w, p, 'soft'))
                w = Train.trainw(w, p, params[1])
            # print(str(w))
            weights.append(w)
            if self.addterr(self.calcsofterror(w, self.test, params[2]), w) < params[4]:
                break
        return weights

    # produced the confusion matrix and calculates the accuracy for the best weights
    def calcconfusion(self):
        tfemale = 0
        tmale = 0
        ffemale = 0
        fmale = 0
        for p in self.test:
            if Train.cnet(self.bestw, p, 'hard') == Person.FEMALE:
                if p.sex == Person.FEMALE:
                    tfemale += 1
                else:
                    ffemale += 1
            else:
                if p.sex == Person.MALE:
                    tmale += 1
                else:
                    fmale += 1

        print("Confusion Matrix ", self.kind.capitalize(), " Transition")
        print("\t| PF | PM ")
        print("AF: |", tfemale, "|", fmale)
        print("AM: |", ffemale, "|", tmale)
        print("accuracy: ", "{0:.3f}%".format(float(tfemale + tmale)/float(tmale+tfemale+ffemale+fmale)*100))
        print("best weights: ", self.bestw, "terr: ", self.besterr, "\n")

    # checks if the current error is the lowest error found so far
    def checkbest(self, terr, w):
        if terr < self.besterr:
            self.besterr = terr
            self.bestw = w

    # calculates the total error for the soft activation function for the weights and people sent in
    def calcsofterror(self, w, people, k):
        terr = 0
        for p in people:
            terr += (Train.fbip(k, Train.cnet(w, p, 'soft')) - p.sex) ** 2
        self.softerror = terr
        return terr

    # calculates the output of the unit given a gain and the net
    @staticmethod
    def fbip(k, x):
        return 1/(1 + exp(-1 * k * x))

    # calculates the net value for both hard and soft usage
    # the hard version is used for calculating the confusion matrices and the accuracy
    @staticmethod
    def cnet(w, p, type):
        if type == 'hard':
            if p.height * w[0] + p.weight * w[1] + w[2] >= 0:
                return Person.FEMALE
            else:
                return Person.MALE
        else:
            return p.height * w[0] + p.weight * w[1] + w[2]

    # trains the weights given the current weights, pattern, and alpha assuming the pattern carries the
    # actual output
    @staticmethod
    def trainw(w, p, a):
        err = p.sex - p.pred
        w[0] += a * p.height * err
        w[1] += a * p.weight * err
        w[2] += a * err
        # if abs(w[0]) > 10 or abs(w[1]) > 10 or abs(w[2]) > 10:
        #     for i in range(0, len(w)):
        #         w[i] = w[i]/10
        #     print(w)
        return w

    # splits the input data into a training set and a test set
    # if 0 or 100 are passed as the percent to use all data is loaded to both sets
    def dividedata(self, people, cut, numpeople):
        if cut in (0, 100):
            self.data = people
            self.test = people
        else:
            self.data = people[0:int(numpeople*cut/100)]
            self.test = people[int(numpeople*cut/100): numpeople]

    # adds the current total error to the array of errors and checks if it was the best so far
    def addterr(self, terr, w):
       # print("terr: ", str(terr))
        self.errors.append(terr)
        self.iterations += 1
        self.checkbest(terr, w)
        return terr

    # calculate the total error for a hard activation function using the current weight set
    # and the training data
    def calcharderror(self, w, test):
        terr = 0
        for p in test:
            terr += (Train.cnet(w, p, 'hard') - p.sex) ** 2
        self.harderror = terr
        return terr

