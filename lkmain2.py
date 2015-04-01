import numpy.random as nprnd
import matplotlib.pyplot as plt

numLow = 1
numHigh = 1000
numCities = 50
m = 3

def generatecities(n):
    # Generate the coordinates of n random cities
    xcities = []
    ycities = []
    for x in range (0, n):
        xcities.append(nprnd.randint(numLow, numHigh))
        ycities.append(nprnd.randint(numLow, numHigh))
    return [xcities, ycities]

def plotcities(opttour):
    #Plots the cities on a square
    #Input: list of 2 lists with x,y coordinates on each list
    xy1 = xys[0][:]
    xy2 = xys[1][:]
    #Sort according to latest tour optimization
    xy1 = [xy1 for (opttour, xy1) in sorted(zip(opttour, xy1))]
    xy2 = [xy2 for (opttour, xy2) in sorted(zip(opttour, xy2))]
    #Make it a cycle
    xy1.append(xy1[0])
    xy2.append(xy2[0])
    plt.plot(xy1, xy2, linestyle = '-', marker ='o', color = 'b', markerfacecolor = 'red')
    plt.ylabel('original path')
    plt.show()




def linkernighan(xys, optlist):
    #Check for every pair of cities that are neighbors in the tour whether improvement can be found

        #Given a pair of cities, find the swap that attains minimum distance with respect to current tour





def swapcities(tour, cb, ce):
    
#Generate cities
xys = generatecities(numCities)
#Generate initial tour
optlist = list(range(1, numCities + 1))

#linkernighan(xys, optlist)

plotcities(optlist)

