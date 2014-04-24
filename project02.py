import itertools

def main():
   #Builds the array containing the distances between cities.
    pathArray, size = openFile()

    #pathArray = initialArray()
    #Generates all permutations possible between the cities.
    allPermutations = getPerms(pathArray, size)
    #Calculates the cost of each set of permutations.
    finalCost = calcPerm(allPermutations, pathArray, size)
    #Sorts the list so the lowest cost is the first element in the array/
    sortedCost = sort(finalCost)
    #Prints the final results.
    printStatement(sortedCost)

def openFile():
    initialArray = []
    counter = 0
    ins = open( "array.txt", "r" )
    for line in ins:
        num = ""
        array = []
        for char in line:
            if(char != ' ' and char != '\n'):
                num = num + char
            else:
                num = float(num)
                array.append(num)
                num = ""
        initialArray.append(array)
        counter += 1
    ins.close()
    return initialArray, counter
def printStatement(sortedCost):
    data = sortedCost[0]
    print("The path with the lowest cost is", data[1],", and the cost is: $",data[0],".")

def sort(finalCost):
    finalCost.sort()
    return finalCost

def calcPerm(allPermutations, pathArray, size):
    finalCost = []
    for perm in allPermutations:
        data = []
        cost = findCost(perm, pathArray, size)
        data.append(cost)
        data.append(perm)
        finalCost.append(data)
    return finalCost

def getPerms(pathArray, size):
    allPermutations = []
    for p in itertools.permutations(range(1, size+1)):
        allPermutations.append(p)
    return allPermutations

def findCost(perm, pathArray, size):
   cost = 0
   for idx in range (size -1):
       cost += pathArray[perm[idx]-1][perm[idx+1]-1]
   cost += pathArray[perm[size-1]-1][perm[0]-1]
   return cost


def initialArray():
    pathArray = [[-1, 1.3, 5.3, 2.6],
                [3.4, -1, 7.1, 3.1],
                [5.3, 4.8, -1, 5.2],
                [8.2, 11.2, 3.9, -1]]
    return pathArray






main()
