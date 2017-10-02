from src.Data.Person import Person
import numpy.random

people = []

for i in range(0, 40):
    if i < 20:
        s = 0
    else:
        s = 1
    a = Person(numpy.random.normal(0, 1), numpy.random.normal(0, 1), s)
    people.append(a)

f = open('data.txt', 'w')
for p in people:
    f.write(str(p.height) + "," + str(p.weight) + "," + str(p.sex) + "\n")

f.close()


