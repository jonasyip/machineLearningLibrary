#k-mean clustering

import random
import math
import time

def getRandomValue(MaxValue): #Returns two random data points
    value = random.randint(0,MaxValue) 
    return value

def hasClusterChanged(prev, curr):
    if len(prev) != len(curr):
        return False

    for i in range(len(prev)):
        for j in range(len(prev)):
            if prev[i][j] != curr[i][j]:
                return False
    return True


def getEuclideanDistance(point_1,point_2):
    holdValue = 0

    for i in range(len(point_1)):
        holdValue +=((point_1[i] - point_2[i])**2)

    return math.sqrt(holdValue)
    
def getAverageVector(points):
    averageVector = []

    for coloumn in range(len(points[0])):
        averageVectorDem = []
        for rows in range(len(points)):  
            averageVectorDem.append(points[rows][coloumn])
        averageVector.append(sum(averageVectorDem)/len(points))
    
    return averageVector
        
'''
def getCluster(DataPoints,Reference_Priority,Reference_Compare):
    Cluster = []
    Cluster.append(Reference_Priority)
    for i in range(len(DataPoints)):
        if (Reference_Priority != Reference_Compare) and (Reference_Priority != DataPoints[i]) and (Reference_Compare!=DataPoints[i]):  
            if getNuclideanDistance(Reference_Priority,DataPoints[i]) < getNuclideanDistance(Reference_Compare,DataPoints[i]):
                Cluster.append(DataPoints[i])
'''
def isInCluster(clusterNumber,referencePoints,dataPoint):
    #Get distance of Reference point 1 to datapoint
    #get list of distances of all the other points from the data point
    #if index is num, and reference point num is the smallest distance, return true
    #print("referencePoints", referencePoints)
    listOfDistances = [getEuclideanDistance(aPoint,dataPoint) for aPoint in referencePoints]

    return listOfDistances.index(min(listOfDistances)) == clusterNumber   
    
#========================================================================================  
def test_isInCluster():
    #Returns a cluster 
    #Data = [[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7],[5,6,7,8]]
    Data = [3,4,5,6]
    Ref_Points = [[1,2,3,4],[2,3,4,5]]
    Index = 2
    expected_result = True  
    actual_result = isInCluster(Index, Ref_Points, Data) 
    assert expected_result == actual_result
    
    
    expected_result = False
    Ref_Points = [[2,3,4,5],[1,2,3,4]]
    actual_result = isInCluster(Index, Ref_Points, Data)
    assert expected_result == actual_result

    
    Ref_Points = [[1,2],[12,13]]
    Data = [2,3]
    Index = 1
    expected_result = True
    actual_result = isInCluster(Index, Ref_Points, Data)
    assert expected_result == actual_result
    

def test_compareTwoDistances():
    #Returns true if first distance is greater than second distance
    Distance_1 = 10
    Distance_2 = 3
    expected_result = True
    actual_result = isDistanceGreater(Distance_1,Distance_2)
    assert expected_result == actual_result
    
def test_getAverageVector():
    #Calculates the mean coordiantes, it should return the mean coordinates 2D
    Cluster = [[1,2],[2,3],[3,4],[4,5],[5,6]]
    expected_result = [3,4]
    actual_result = getAverageVector(Cluster)
    print(actual_result)
    assert expected_result == actual_result

    #Calculates the mean coordiantes, it should return the mean coordinates 3D
    Cluster = [[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7]]
    expected_result = [3,4,5]
    actual_result = getAverageVector(Cluster)
    print(actual_result)
    assert expected_result == actual_result
    
def test_getNuclideanDistance():
    #using pythagoras, it should return a correct distance in 4D
    p1 = [8,8,8,8]
    p2 = [6,6,6,6]
    expected_result = 4
    actual_result = getEuclideanDistance(p1,p2)
    assert expected_result == actual_result

    #using pythagoras, it should return a correct distance in 2D
    p1 = [15,21]
    p2 = [11,18]
    expected_result = 5
    actual_result = getEuclideanDistance(p1,p2)
    assert expected_result == actual_result

def test_hasClusterChanged(): 
    #if the two cluster length is different, it should return false
    prev_cluster = [[1,2],[2,1]]
    curr_cluster = [[3,1]]
    expected_result = False
    # expect hasClusterChanged(prev, curr) to False
    actual_result = hasClusterChanged(prev_cluster, curr_cluster)
    assert expected_result == actual_result

    #if the clusters are identical, it  should return true
    prev_cluster = [[1,2],[2,1]]
    curr_cluster = [[1,2],[2,1]]
    expected_result = True
    actual_result = hasClusterChanged(prev_cluster, curr_cluster)
    assert expected_result == actual_result

    #if the clusters are identical in length,
    # if the cluster points are different, it should return false
    #this is a worst case scenio
    curr_cluster = [[1,2],[2,2]]
    expected_result = False
    actual_result = hasClusterChanged(prev_cluster, curr_cluster)
    assert expected_result == actual_result
    
#========================================================================================

def kMean(data, k):
    current_Cluster = []
    previous_Cluster = []
    referencePoints = []
    clusters = []
    numberOfClusters = k
    means = []

    for k in range(numberOfClusters):
        hasTheClusterChanged = True
        if k >= len(clusters):
            clusters.append([])
            means.append([])

        
        while hasTheClusterChanged:

            scrambledDataPoints = random.sample(data,len(data))
            referencePoints = scrambledDataPoints[0:numberOfClusters]
            clusterK = []
            
            for j in range(len(data)):
                if isInCluster(k, referencePoints, data[j]):
                    clusterK.append(data[j])
                
            hasTheClusterChanged = hasClusterChanged(clusterK,clusters[k])

            clusters[k] = clusterK

            means[k] = getAverageVector(clusterK)
            

    return means

def predict(point , means):
    categories = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica', 'Iris-bogus', 'five', 'six', 'seven']
    distances = [getEuclideanDistance(aPoint,point) for aPoint in means]
    index = distances.index(min(distances))

    return categories[index]


if __name__ == '__main__':
    data = [
        [5.1,3.5,1.4,0.2],
        [4.9,3,1.4,0.2],
        [4.7,3.2,1.3,0.2],
        [4.6,3.1,1.5,0.2],
        [5,3.6,1.4,0.2],
        [5.4,3.9,1.7,0.4],
        [4.6,3.4,1.4,0.3],
        [5,3.4,1.5,0.2],
        [4.4,2.9,1.4,0.2],
        [4.9,3.1,1.5,0.1],
        [5.4,3.7,1.5,0.2],
        [4.8,3.4,1.6,0.2],
        [4.8,3,1.4,0.1],
        [4.3,3,1.1,0.1],
        [5.8,4,1.2,0.2],
        [5.7,4.4,1.5,0.4],
        [5.4,3.9,1.3,0.4],
        [5.1,3.5,1.4,0.3],
        [5.7,3.8,1.7,0.3],
        [5.1,3.8,1.5,0.3],
        [5.4,3.4,1.7,0.2],
        [5.1,3.7,1.5,0.4],
        [4.6,3.6,1,0.2],
        [5.1,3.3,1.7,0.5],
        [4.8,3.4,1.9,0.2],
        [5,3,1.6,0.2],
        [5,3.4,1.6,0.4],
        [5.2,3.5,1.5,0.2],
        [5.2,3.4,1.4,0.2],
        [4.7,3.2,1.6,0.2],
        [4.8,3.1,1.6,0.2],
        [5.4,3.4,1.5,0.4],
        [5.2,4.1,1.5,0.1],
        [5.5,4.2,1.4,0.2],
        [4.9,3.1,1.5,0.1],
        [5,3.2,1.2,0.2],
        [5.5,3.5,1.3,0.2],
        [4.9,3.1,1.5,0.1],
        [4.4,3,1.3,0.2],
        [5.1,3.4,1.5,0.2],
        [5,3.5,1.3,0.3],
        [4.5,2.3,1.3,0.3],
        [4.4,3.2,1.3,0.2],
        [5,3.5,1.6,0.6],
        [5.1,3.8,1.9,0.4],
        [4.8,3,1.4,0.3],
        [5.1,3.8,1.6,0.2],
        [4.6,3.2,1.4,0.2],
        [5.3,3.7,1.5,0.2],
        [5,3.3,1.4,0.2],
        [7,3.2,4.7,1.4],
        [6.4,3.2,4.5,1.5],
        [6.9,3.1,4.9,1.5],
        [5.5,2.3,4,1.3],
        [6.5,2.8,4.6,1.5],
        [5.7,2.8,4.5,1.3],
        [6.3,3.3,4.7,1.6],
        [4.9,2.4,3.3,1],
        [6.6,2.9,4.6,1.3],
        [5.2,2.7,3.9,1.4],
        [5,2,3.5,1],
        [5.9,3,4.2,1.5],
        [6,2.2,4,1],
        [6.1,2.9,4.7,1.4],
        [5.6,2.9,3.6,1.3],
        [6.7,3.1,4.4,1.4],
        [5.6,3,4.5,1.5],
        [5.8,2.7,4.1,1],
        [6.2,2.2,4.5,1.5],
        [5.6,2.5,3.9,1.1],
        [5.9,3.2,4.8,1.8],
        [6.1,2.8,4,1.3],
        [6.3,2.5,4.9,1.5],
        [6.1,2.8,4.7,1.2],
        [6.4,2.9,4.3,1.3],
        [6.6,3,4.4,1.4],
        [6.8,2.8,4.8,1.4],
        [6.7,3,5,1.7],
        [6,2.9,4.5,1.5],
        [5.7,2.6,3.5,1],
        [5.5,2.4,3.8,1.1],
        [5.5,2.4,3.7,1],
        [5.8,2.7,3.9,1.2],
        [6,2.7,5.1,1.6],
        [5.4,3,4.5,1.5],
        [6,3.4,4.5,1.6],
        [6.7,3.1,4.7,1.5],
        [6.3,2.3,4.4,1.3],
        [5.6,3,4.1,1.3],
        [5.5,2.5,4,1.3],
        [5.5,2.6,4.4,1.2],
        [6.1,3,4.6,1.4],
        [5.8,2.6,4,1.2],
        [5,2.3,3.3,1],
        [5.6,2.7,4.2,1.3],
        [5.7,3,4.2,1.2],
        [5.7,2.9,4.2,1.3],
        [6.2,2.9,4.3,1.3],
        [5.1,2.5,3,1.1],
        [5.7,2.8,4.1,1.3],
        [6.3,3.3,6,2.5],
        [5.8,2.7,5.1,1.9],
        [7.1,3,5.9,2.1],
        [6.3,2.9,5.6,1.8],
        [6.5,3,5.8,2.2],
        [7.6,3,6.6,2.1],
        [4.9,2.5,4.5,1.7],
        [7.3,2.9,6.3,1.8],
        [6.7,2.5,5.8,1.8],
        [7.2,3.6,6.1,2.5],
        [6.5,3.2,5.1,2],
        [6.4,2.7,5.3,1.9],
        [6.8,3,5.5,2.1],
        [5.7,2.5,5,2],
        [5.8,2.8,5.1,2.4],
        [6.4,3.2,5.3,2.3],
        [6.5,3,5.5,1.8],
        [7.7,3.8,6.7,2.2],
        [7.7,2.6,6.9,2.3],
        [6,2.2,5,1.5],
        [6.9,3.2,5.7,2.3],
        [5.6,2.8,4.9,2],
        [7.7,2.8,6.7,2],
        [6.3,2.7,4.9,1.8],
        [6.7,3.3,5.7,2.1],
        [7.2,3.2,6,1.8],
        [6.2,2.8,4.8,1.8],
        [6.1,3,4.9,1.8],
        [6.4,2.8,5.6,2.1],
        [7.2,3,5.8,1.6],
        [7.4,2.8,6.1,1.9],
        [7.9,3.8,6.4,2],
        [6.4,2.8,5.6,2.2],
        [6.3,2.8,5.1,1.5],
        [6.1,2.6,5.6,1.4],
        [7.7,3,6.1,2.3],
        [6.3,3.4,5.6,2.4],
        [6.4,3.1,5.5,1.8],
        [6,3,4.8,1.8],
        [6.9,3.1,5.4,2.1],
        [6.7,3.1,5.6,2.4],
        [6.9,3.1,5.1,2.3],
        [5.8,2.7,5.1,1.9],
        [6.8,3.2,5.9,2.3],
        [6.7,3.3,5.7,2.5],
        [6.7,3,5.2,2.3],
        [6.3,2.5,5,1.9],
        [6.5,3,5.2,2],
        [6.2,3.4,5.4,2.3],
        [5.9,3,5.1,1.8]]
    timeStart = time.time()
    means = kMean(data, 7)
    print("time taken",time.time()-timeStart)
    print (predict([5.1,3.4,1.5,0.2], means))
    print (predict([5.9, 3.0, 5.1, 1.8], means))
    print (predict([6.7,3,5.2,2.3], means))

    print (predict([3.2, 7.2, 5, 10.1], means))


