from src.Data.Person import Person
from src.Data.normalize import normalize

people = normalize(Person.makepeople(400))


w = [1, 1, -1]
k = .02

print(str(people[2].height))

for i in range(0, 400):
    for p in people:
        if p.height * w[0] + p.weight * w[1] + w[2] < 0:
            net = -1
        else:
            net = 1
        w[0] += k * p.height * (p.sex - net)
        w[1] += k * p.weight * (p.sex - net)
        w[2] += k * (net - p.sex)
    print(str(w))


f = open('data.txt', 'w')
for p in people:
    f.write(str(p.height) + "," + str(p.weight) + "," + str(p.sex) + "\n")

f.close()


