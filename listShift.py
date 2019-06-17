class Solution(object):
    def rotate(self, nums, k):
        if(k ==0):
            return nums
        inflection = len(nums)-k
        nums[:] = nums[inflection:]+nums[:inflection]
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        