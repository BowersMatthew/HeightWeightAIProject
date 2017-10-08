from src.Data.Person import Person
from src.graph.coolgraph import coolgraph
from src.Data.normalize import minmaxnorm
from src.training.train import Train
from multiprocessing import Process

if __name__ == '__main__':
    numpeople = 4000
    # percent to use for training
    cut = 50
    people = minmaxnorm(Person.makepeople(numpeople))
    # hard params order should be [starting weights, alpha, max iterations, desired error, cut, num people]
    params = [[1, 1, 1], 0.05, 1000, 0.00001, cut, numpeople]
    hard = Train(people, params)
    p = Process(target=coolgraph, args=(hard.test, hard.bestw, 'hard'))
    p.start()

    # soft params order should be [starting weights, alpha, gain, max iterations, desired error, cut, num people]
    params = [[1, 1, 1], 2, 0.005, 1000, 0.00001, cut, numpeople]
    soft = Train(people, params)
    p1 = Process(target=coolgraph, args=(soft.test, soft.bestw, 'soft'))
    p1.start()
    p.join()
    p1.join()
    hard.calcconfusion()
    soft.calcconfusion()
