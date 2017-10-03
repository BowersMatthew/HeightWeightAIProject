from src.Data.Person import Person


def normalize(people):
    sumh = 0
    sumw = 0
    count = 0
    for p in people:
        sumh += p.height
        sumw += p.weight
        count += 1
    avgh = sumh/count
    avgw = sumw/count

    sumhdiff = 0
    sumwdiff = 0
    for p in people:
        sumhdiff += (p.height - avgh) ** 2
        sumwdiff += (p.weight - avgw) ** 2

    sdh = (sumhdiff/(count - 1)) ** 0.5
    sdw = (sumwdiff/(count - 1)) ** 0.5

    for p in people:
        p.height = (p.height - avgh) / sdh
        p.weight = (p.weight - avgw) / sdw

    return people


def minmaxnorm(people):
    for p in people:
        p.height = (p.height - Person.minh) / (Person.maxh - Person.minh)
        p.weight = (p.weight - Person.minw) / (Person.maxw - Person.minw)
    return people
