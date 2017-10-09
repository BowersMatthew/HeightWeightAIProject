from src.Data.Person import Person
from src.Data.writer import tofile
from src.graph.coolgraph import coolgraph
from src.Data.normalize import minmaxnorm
from src.training.train import Train
from multiprocessing import Process
from src.graph.errorgraph import errorgraph
import numpy.random
import os

if __name__ == '__main__':
    # number of people in the whole data set
    numpeople = 4000
    hardsets = []
    softsets = []

    # generate the people
    people = Person.makepeople(numpeople)

    # write the people to file
    towrite = ''
    for p in people:
        towrite += str(p)
    tofile(os.path.join(os.path.realpath(''), '..\\..\\data\\data.txt'), towrite)

    # normalize the people
    people = minmaxnorm(people)

    for cut in (75, 50, 25):
        # percent to use for training
        # cut = 50
        # hard params order should be [starting weights, alpha, max iterations, desired error, cut, num people]
        params = [[numpy.random.normal(0, 1), numpy.random.normal(0, 1), numpy.random.normal(0, 1)], 0.05, 1000, 0.00001, cut, numpeople]
        print("Training hard")
        hard = Train(people, params)
        hardsets.append(hard)
        # write this result to file
        print("Writing Results")
        tofile(os.path.join(os.path.realpath(''),
                            ('..\\..\\data\\hard' + str(cut) + str(100 - cut) + ".txt")), str(hard.bestw)[1:-1])

        # spin a thread to graph the result
        print("Creating graph")
        p = Process(target=coolgraph, args=(hard.test, hard.bestw, hard))
        e = Process(target=errorgraph, args=(hard,))


        # soft params order should be [starting weights, alpha, gain, max iterations, desired error, cut, num people]
        params = [[numpy.random.normal(0, 1), numpy.random.normal(0, 1), numpy.random.normal(0, 1)], 0.1, 0.005, 1000, 0.00001, cut, numpeople]
        print("Training soft")
        soft = Train(people, params)
        softsets.append(soft)
        # write this result to file
        print("Writing results")
        tofile(os.path.join(os.path.realpath(''),
                            ('..\\..\\data\\soft' + str(cut) + str(100 - cut) + ".txt")), str(soft.bestw)[1:-1])

        # spin a thread to graph the result
        print("Creating graph")
        p1 = Process(target=coolgraph, args=(soft.test, soft.bestw, soft))
        e1 = Process(target=errorgraph, args=(soft,))
        print("Displaying graph")
        p.start()
        e.start()
        p1.start()
        e1.start()
        p.join()
        p1.join()
        e.join()
        e1.join()

    print("Generating confusion matrices")
    for h in hardsets:
        h.calcconfusion()
    for s in softsets:
        s.calcconfusion()

