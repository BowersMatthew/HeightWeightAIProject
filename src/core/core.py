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
# print(str(people[2].height))

for i in range(0, 4000):
    for p in people:
        if p.height * w[0] + p.weight * w[1] + w[2] < 0:
            net = 0
        else:
            net = 1
        w[0] += a * p.height * (p.sex - net)
        w[1] += a * p.weight * (p.sex - net)
        w[2] += a * (p.sex - net)
    print(str(w))


f = open('data.txt', 'w')
for p in people:
    f.write(str(p.height) + "," + str(p.weight) + "," + str(p.sex) + "," + str(p.pred) + "\n")

f.close()
coolgraph(people)


