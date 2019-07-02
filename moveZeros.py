class Solution(object):
    def moveZeroes(self, nums):
        for index in range(len(nums)-1,0,-1):
            if(nums[index] == 0):
                del nums[index]
                nums.append(0)      
        if(nums[0] == 0):
            del nums[0]
            nums.append(0)
            
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        