from src.Data.Person import Person
from src.Data.normalize import normalize

people = normalize(Person.makepeople(4000))


w = [1, 1, 1]
a = .001

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
    f.write(str(p.height) + "," + str(p.weight) + "," + str(p.sex) + "\n")

f.close()


