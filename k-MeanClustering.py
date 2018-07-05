#k-mean clustering

import random
import math

def calculateAverageVector(clusterList = []):
    averageVectorList = []
    for i in range(0,len(clusterList[0])): #From first element to last element
        valuePoint = 0
        for j in range(0,len(clusterList)):
            valuePoint = valuePoint + int(clusterList[j][i])
            #print(valuePoint)
        averagePoint = valuePoint / len(clusterList)
        averageVectorList.append(averagePoint) #Stores the ordinate in a list [i,j,k,l]
    #print(averageVectorList)
    return averageVectorList #Return vector coodinates

def produceRandomReferencePoint(numberOfDataPoints): #Returns two random data points
    referencePointOne = random.randint(0,numberOfDataPoints)
    referencePointTwo = random.randint(0,numberOfDataPoints)
    while referencePointOne == referencePointTwo: #Prevents two data point references have the same value
        referencePointTwo = random.randint(0,numberOfDataPoints)    
    return [referencePointOne,referencePointTwo]

def distanceBetweenTwoPoints(coodinate_1 = [], coodinate_2 = []): #This function returns a value length between two points
    holdValue = 0
    for i in range(0,len(coodinate_1)):
        holdValue = holdValue + ((coodinate_2[i] - coodinate_1[i])**2)
        print(holdValue)
    return math.sqrt(holdValue)
        
def compareTwoDistances(distance_1, distance_2,fromReferencePoint): #
    if (distance_1 > distance_2 and fromReferencePoint):
        a=1
        
    

testData =[[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7],[5,6,7,8]]



print(calculateAverageVector(testData))
print(produceRandomReferencePoint(len(testData)))
print(distanceBetweenTwoPoints([1,2,3,4],[4,3,2,1]))
