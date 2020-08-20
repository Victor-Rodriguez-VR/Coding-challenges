class Solution(object):
    def containsDuplicate(self, nums):
        trueNumbers = set(nums) # Creates a set from the given list. Sets by nature have no duplicates.
        if(len(trueNumbers) == len(nums)): # If a set and the given list have the same size - that means no duplicates were excluded from the list to set conversion.
            return False # Aka no duplicates.
        return True # Otherwise returns true.
        
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        :type nums: List[int]
        :rtype: bool
        """
        
        
