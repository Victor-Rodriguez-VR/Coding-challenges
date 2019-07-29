class Solution(object):
    def containsDuplicate(self, nums):
        # Initiates a no-duplicate environment
        trueNumbers = set()
        for number in nums:
            # If found a duplicate within trueNumbers, immidiately returns true.
            if number in trueNumbers:
                return True
            # Otherwise adds the number to trueNumbers.
            else:
                trueNumbers.add(number)
        # If no duplicate was found, returns false.
        return False
        
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        