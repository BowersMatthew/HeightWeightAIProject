import numpy.random


class Person(object):
    # markers for gender
    MALE = -1
    FEMALE = 1
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
        if gender == self.MALE:
            self.height = (zh * self.maleSdHeight) + self.maleAveHeight
            self.weight = (zw * self.maleSdBMI + self.maleAveBMI) * self.height / 100 * self.height / 100
            self.sex = gender
        else:
            self.height = (zh * self.femaleSdHeight) + self.femaleAveHeight
            self.weight = (zw * self.femaleSdBMI + self.femaleAveBMI) * self.height / 100 * self.height / 100
            self.sex = gender

    # generates and returns and array of num people with 50:50 split m/w random normal distro of attributes
    @staticmethod
    def makepeople(num):
        people = []

        for i in range(0, num):
            if i % 2 == 0:
                s = -1
            else:
                s = 1
            people.append(Person(numpy.random.normal(0, 1), numpy.random.normal(0, 1), s))

        return people
