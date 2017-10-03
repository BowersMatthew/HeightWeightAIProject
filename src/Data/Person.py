import numpy.random


class Person(object):
    # markers for gender
    MALE = 0
    FEMALE = 1

    # max and min values for normalizing
    maxw = 0
    minw = 1000
    maxh = 0
    minh = 1000

    # in cm
    # these constants are derived from the WHO standard growth charts
    maleAveHeight = 176.5
    maleSdHeight = 6.2
    femaleAveHeight = 163.3
    femaleSdHeight = 5.5
    # Block, J. P., Subramanian, S. V., Christakis, N. A., & O�Malley,
    # A. J. (2013). Population Trends and Variation in Body Mass Index
    # from 1971 to 2008 in the Framingham Heart Study Offspring Cohort.
    # PLoS ONE, 8(5), e63217. http://doi.org/10.1371/journal.pone.0063217
    # kg/m/m
    maleAveBMI = 29
    maleSdBMI = 4.73
    femaleAveBMI = 27.7
    femaleSdBMI = 6.15

    def __init__(self, zh, zw, gender):
        self.pred = gender
        if gender == self.MALE:
            self.height = (zh * Person.maleSdHeight) + Person.maleAveHeight
            self.weight = (zw * Person.maleSdBMI + Person.maleAveBMI) * self.height / 100 * self.height / 100
            self.sex = gender
        else:
            self.height = (zh * Person.femaleSdHeight) + Person.femaleAveHeight
            self.weight = (zw * Person.femaleSdBMI + Person.femaleAveBMI) * self.height / 100 * self.height / 100
            self.sex = gender
        Person.check(self)

    # checks if the person just created has a min or max attribute'
    @staticmethod
    def check(p):
        if p.weight > Person.maxw:
            Person.maxw = p.weight
        if p.weight < Person.minw:
            Person.minw = p.weight
        if p.height > Person.maxh:
            Person.maxh = p.height
        if p.height < Person.minh:
            Person.minh = p.height

    # generates and returns and array of num people with 50:50 split m/w random normal distro of attributes
    @staticmethod
    def makepeople(num):
        people = []

        for i in range(0, num):
            if i % 2 == 0:
                s = Person.MALE
            else:
                s = Person.FEMALE
            people.append(Person(numpy.random.normal(0, 1), numpy.random.normal(0, 1), s))

        return people
