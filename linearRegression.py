import math


def variance(numberOfValues,sumFrequencyX,sumFrequencyXSquared):
    return ((sumFrequencyXSquared/numberOfValues)-((sumFrequencyX/numberOfValues)**2))



def mean(values):
    return sum(values) / len(values)

def test_Mean():
    #passing a list of values which the function return its mean average
    values = [5,5,5,5,5]
    expectedResult = 5
    actualResult = mean(values)
    assert expectedResult == actualResult

def test_variance():
    expectedResult = 2
    actualResult = variance(5,15,55)
    assert expectedResult == actualResult
    


test_variance()
