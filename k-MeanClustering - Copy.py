#k-mean clustering

import random
import math

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
    print("P",points)
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

TESTDATA =[[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7],[5,6,7,8]]
current_Cluster = []
previous_Cluster = []
referencePoints = []
clusters = []
numberOfClusters = 2
means = []

for k in range(numberOfClusters):
    hasTheClusterChanged = True
    if k >= len(clusters):
        clusters.append([])
        means.append([])

    
    while hasTheClusterChanged:

        scrambledDataPoints = random.sample(TESTDATA,len(TESTDATA))
        referencePoints = scrambledDataPoints[0:numberOfClusters]
        print(referencePoints)
        clusterK = []
        
        for j in range(len(TESTDATA)):

            if isInCluster(k, referencePoints, TESTDATA[j]):
                clusterK.append(TESTDATA[j])

            
        hasTheClusterChanged = hasClusterChanged(clusterK,clusters[k])

        clusters[k] = clusterK

        means[k] = getAverageVector(clusterK)
        print("Means",means)


