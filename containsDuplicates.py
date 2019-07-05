class Solution(object):
    def containsDuplicate(self, nums):
        trueNumbers = set()
        for number in nums:
            if number in trueNumbers:
                return True
            else:
                trueNumbers.add(number)
        return False
        
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        