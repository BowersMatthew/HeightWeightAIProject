from src.Data.Person import Person
from src.graph.coolgraph import coolgraph
from src.Data.normalize import minmaxnorm
from src.training.train import Train


people = minmaxnorm(Person.makepeople(4000))
params = [[1, 1, 1], 0.01, 400, 0.00001]
hard = Train(people, params)

for e in hard.errors:
    print(str(e))
print("Best weight: " + str(hard.bestw) + "Best err:" + str(hard.besterr))

f = open('data.txt', 'w')
for p in people:
    f.write(str(p.height) + "," + str(p.weight) + "," + str(p.sex) + "," + str(p.pred) + "\n")

f.close()

coolgraph(people)


