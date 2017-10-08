from src.Data.Person import Person
from math import exp


class Train:

    def __init__(self, people, params):
        self.iterations = 0
        self.errors = []
        self.besterr = 100000
        self.bestw = []
        self.data = []
        self.test = []
        if len(params) == 6:
            self.weights = Train.hard(self, people, params)
        elif len(params) == 7:
            self.weights = Train.soft(self, people, params)
        else:
            print("Invalid number of params")

    # params order should be [starting weights, alpha, max iterations, desired error, cut, num people]
    def hard(self, people, params):
        self.dividedata(people, params[4], params[5])
        # self.data = people[0:params[4]]
        # self.test = people[params[4]:4000]
        w = params[0]
        self.bestw = w
        weights = [w]
        for i in range(0, params[2]):
            for p in self.data:
                p.pred = Train.cnet(w, p, 'hard')
                w = Train.trainw(w, p, params[1])
            # print(str(w))
            weights.append(w)
            terr = Train.calcharderror(w, self.test)
            print(str(terr))
            self.errors.append(terr)
            self.iterations += 1
            self.checkbest(terr, w)
            if terr < params[3]:
                break
        return weights

    @staticmethod
    def calcharderror(w, test):
        terr = 0
        for p in test:
            terr += (Train.cnet(w, p, 'hard') - p.sex) ** 2
        return terr

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
            terr = Train.calcsofterror(w, self.test, params[2])
            # print(str(w))
            weights.append(w)
            print("terr: ", str(terr))
            self.errors.append([i, terr])
            self.iterations += 1
            self.checkbest(terr, w)
            if terr < params[4]:
                break
        return weights

    def checkbest(self, terr, w):
        if terr < self.besterr:
            self.besterr = terr
            self.bestw = w

    @staticmethod
    def calcsofterror(w, people, k):
        terr = 0
        for p in people:
            terr += (Train.fbip(k, Train.cnet(w, p, 'soft')) - p.sex) ** 2
        return terr

    @staticmethod
    def fbip(k, x):
        return 1/(1 + exp(-1 * k * x))

    @staticmethod
    def cnet(w, p, type):
        if type == 'hard':
            if p.height * w[0] + p.weight * w[1] + w[2] >= 0:
                return Person.FEMALE
            else:
                return Person.MALE
        else:
            return p.height * w[0] + p.weight * w[1] + w[2]

    @staticmethod
    def trainw(w, p, a):
        err = p.sex - p.pred
        w[0] += a * p.height * err
        w[1] += a * p.weight * err
        w[2] += a * err
        return w

    def dividedata(self, people, cut, numpeople):
        if cut in (0, 100):
            self.data = people
            self.test = people
        else:
            self.data = people[0:int(numpeople*cut/100)]
            self.test = people[int(numpeople*cut/100): numpeople]

