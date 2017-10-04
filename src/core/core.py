from src.Data.Person import Person
from src.graph.coolgraph import coolgraph
from src.Data.normalize import minmaxnorm
from src.training.train import Train


people = minmaxnorm(Person.makepeople(4000))
params = [[1, 1, 1], 0.01, 1000, 0.00001]
hard = Train(people, params)
coolgraph(hard.data, hard.bestw)

params = [[1, 1, 1], .01, 1, 1000, 0.00001]
soft = Train(people, params)
coolgraph(soft.data, soft.bestw)
