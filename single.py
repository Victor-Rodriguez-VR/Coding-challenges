class Solution(object):
    def singleNumber(self, nums):
        singleSet = sum((nums))
        doubleSet = 2* sum (set(nums))
        return doubleSet - singleSet
        