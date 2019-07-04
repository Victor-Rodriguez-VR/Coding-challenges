def findSmallestNumber(inputList):
    currentSmallest = 0
    for index in range(1,inputList):
        if(inputList[index] < inputList[index-1]):
            return index
    return 0
