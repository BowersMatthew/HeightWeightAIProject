from math import exp

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
        self.data = people
        w = params[0]
        self.bestw = w
        weights = [w]
        for i in range(0, params[2]):
            for p in self.data:
                if p.height * w[0] + p.weight * w[1] + w[2] < 0:
                    p.pred = 0
                else:
                    p.pred = 1
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
        self.data = people
        w = params[0]
        self.bestw = w
        weights = [w]

        for i in range(0, params[3]):
            terr = 0
            for p in self.data:
                x = p.height * w[0] + p.weight * w[1] + w[2]
                p.pred = Train.fbip(params[2], x)
                #print(p.sex - p.pred)
                err = p.sex - p.pred

                w[0] += params[1] * p.height * (err)
                w[1] += params[1] * p.weight * (err)
                w[2] += params[1] * (err)
                terr += err ** 2
            print(str(w))
            weights.append(w)
            print(str(terr))
            self.errors.append([i, terr])
            self.iterations += 1
            if terr < self.besterr:
                self.besterr = terr
                self.bestw = w
            if terr < params[4]:
                break
        return weights

    @staticmethod
    def calcerror(people):
        terr = 0
        for p in people:
            terr += (p.pred - p.sex) ** 2
        return terr

    @staticmethod
    def fbip(k, x):
        return 1/(1 + exp(-1 * k * x))
