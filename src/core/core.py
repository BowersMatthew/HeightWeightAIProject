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

for p in people:
    print(str(a.height))
    print(str(a.weight))


