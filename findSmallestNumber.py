def findSmallestNumber(inputList):
        # sets up left and right variables.
        left = 0
        right = len(inputList)-1
        smallest = 0
        while left < right-1:
                # Divisble by 2 to fully cut search in half. 
                if( right - left %2 == 0):
                        pivot = int((right-left)/2) + left
                # Otherwise adds a +1 to make the pivot in the middle.
                else:
                        pivot = int((right-left+1)/2 )+ left
                # if pivot < lastSmallest, then smallest should be pivot.
                # and the numbers to search from reduces
                if inputList[pivot] < inputList[smallest]:
                        right = pivot
                        smallest = pivot
                else:
                        left = pivot
        return smallest

