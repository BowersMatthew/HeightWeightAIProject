from src.Data.Person import Person
from src.graph.coolgraph import coolgraph
from src.Data.normalize import minmaxnorm
from src.training.train import Train
from multiprocessing import Process

if __name__ == '__main__':
    people = minmaxnorm(Person.makepeople(4000))
    params = [[1, 1, 1], 0.01, 1000, 0.00001, 2000]
    hard = Train(people, params)
    p = Process(target=coolgraph, args=(hard.data, hard.bestw, 'hard'))
    p.start()

    # params order should be [starting weights, alpha, gain, max iterations, desired error, cut]
    params = [[1, 1, 1], 0.5, 0.01, 1000, 0.00001, 2000]
    soft = Train(people, params)
    p1 = Process(target=coolgraph, args=(soft.data, soft.bestw, 'soft'))
    p1.start()
    p.join()
    p1.join()
