class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        numberMap = {} # Our map that uses numbers as keys and indecies as values.
        for index in range(len(nums)):
            currentNumber = nums[index] # keeps track of the current number
            if currentNumber in numberMap and index - numberMap[currentNumber] <= k: # If the currentNumber is a key in the numberMap, and the index minus the index is associated 
                                                                                    # with the key (currentNumber), then it satisfied both requirements to be true.
                return True
            numberMap[currentNumber] = index # Otherwise creates a new entry in the numberMap with the currentNumber as the key and its index as the value.
 
        return False # If all else fails: its false. 
