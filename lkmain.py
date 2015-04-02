import numpy as np
import scipy.spatial as ssp
import numpy.random as nprnd
import matplotlib.pyplot as plt

numLow = 1
numHigh = 1000
numCities = 20
m = 3
Dist=np.zeros((numCities,numCities))

def generatecities(n):
    # Generate the coordinates of n random cities
    xcities = []
    ycities = []
    nprnd.seed(11)
    for x in range (0, n):
        xcities.append(nprnd.randint(numLow, numHigh))
        ycities.append(nprnd.randint(numLow, numHigh))
    return xcities, ycities

def plotcities(opttour,xys):
    #Plots the cities on a square
    #Input: list of 2 lists with x,y coordinates on each list
    xy1 = xys[0][:]
    xy2 = xys[1][:]
    #Sort according to latest tour optimization
    xy1 = [xy1[i] for i in opttour]
    xy2 = [xy2[i] for i in opttour]
    #Make it a cycle
    xy1.append(xy1[0])
    xy2.append(xy2[0])
    plt.plot(xy1, xy2, linestyle = '-', marker ='o', color = 'b', markerfacecolor = 'red')
    plt.ylabel('original path')




def genDistanceMat(x,y):
    X=np.array([x,y])
    distMat=ssp.distance.pdist(X.T)
    sqdist=ssp.distance.squareform(distMat)
    return sqdist


def calcTourLength(hamPath):
    tourLength=sum(Dist[hamPath[0:-1], hamPath[1:len(hamPath)]])
    tourLength+=Dist[hamPath[-1],hamPath[0]]
    return tourLength


#Generate cities
x,y = generatecities(numCities)    

Dist = genDistanceMat(x, y)
#Generate initial tour
optlist = list(range(0, numCities))
improvement=1
plt.figure(1)
plt.subplot(211)
plotcities(optlist, [x,y])

while (improvement > 0):    #Check for every pair of cities that are neighbors in the tour whether improvement can be found
    bestTourLength = calcTourLength(optlist)
    bestListSoFar = optlist
    improvement = -1
    for i in range(0, len(optlist)):
        #Given a pair of cities, find the swap that attains minimum distance with respect to current tour
        for j in range(2, len(optlist)-1):
            #Do a swap and see if tour length improves
            tempOptList = optlist[0:j]+optlist[:j-1:-1]
            tempTourLength = calcTourLength(tempOptList)
            if(tempTourLength + 10e-12 < bestTourLength):
                improvement = bestTourLength - tempTourLength
                bestListSoFar = tempOptList
                bestTourLength = tempTourLength
        if(bestTourLength+10e-12 < calcTourLength(optlist)):
            optlist = bestListSoFar
            break
        optlist = [optlist[-1]] + optlist[0:-1]
    
print('final optlist: ', optlist)
plt.subplot(212)
plotcities(optlist, [x,y])
plt.show()


