from src.Data.Person import Person

class Train:

    def __init__(self, people, params):
        self.iterations = 0
        self.errors = []
        self.besterr = 100000
        self.bestw = []
        if len(params) == 4:
            self.weights = Train.hard(self, people, params)
        elif len(params) == 5:
            self.weights = Train.soft(self, people, params)
        else:
            print("Invalid number of params")

    # params order should be [starting weights, alpha, max iterations, desired error]
    def hard(self, people, params):
        w = params[0]
        self.bestw = w
        weights = [w]
        for i in range(0, params[2]):
            for p in people:
                if p.height * w[0] + p.weight * w[1] + w[2] < 0:
                    p.pred = Person.MALE
                else:
                    p.pred = Person.FEMALE
                w[0] += params[1] * p.height * (p.sex - p.pred)
                w[1] += params[1] * p.weight * (p.sex - p.pred)
                w[2] += params[1] * (p.sex - p.pred)
            print(str(w))
            weights.append(w)
            terr = Train.calcerror(people)
            print(str(terr))
            self.errors.append(terr)
            self.iterations += 1
            if terr < self.besterr:
                self.besterr = terr
                self.bestw = w
            if terr < params[3]:
                break
        return weights

    # params order should be [starting weights, alpha, gain, max iterations, desired error]
    def soft(self, people, params):
        w = params[0]
        self.bestw = w
        weights = [w]
        for i in range(0, params[3]):
            for p in people:
                if p.height * w[0] + p.weight * w[1] + w[2] < 0:
                    p.pred = Person.MALE
                else:
                    p.pred = Person.FEMALE
                w[0] += params[1] * p.height * (p.sex - p.pred)
                w[1] += params[1] * p.weight * (p.sex - p.pred)
                w[2] += params[1] * (p.sex - p.pred)
            print(str(w))
            weights.append(w)
            terr = Train.calcerror(people)
            print(str(terr))
            self.errors.append(terr)
            self.iterations += 1
            if terr < self.besterr:
                self.besterr = terr
                self.bestw = w
            if terr < params[3]:
                break
        return weights

    @staticmethod
    def calcerror(people):
        terr = 0
        for p in people:
            terr += (p.pred - p.sex) ** 2
        return terr
