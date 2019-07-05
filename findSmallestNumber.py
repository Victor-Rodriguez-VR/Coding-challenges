<<<<<<< HEAD
def findSmallestNumber(inputList):
        left = 0
        right = len(inputList)-1
        smallest = 0
        while left < right-1:
                if( right - left %2 == 0):
                        pivot = int((right-left)/2) + left
                else:
                        pivot = int((right-left+1)/2 )+ left
      
                if inputList[pivot] < inputList[smallest]:
                        right = pivot
                        smallest = pivot
                else:
                        left = pivot
        return smallest

=======
def findSmallestNumber(inputList):
    currentSmallest = 0
    for index in range(1,inputList):
        if(inputList[index] < inputList[index-1]):
            return index
    return 0
>>>>>>> master
