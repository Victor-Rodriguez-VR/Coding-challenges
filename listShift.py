class Solution(object):
    def rotate(self, nums, k):
        if(k ==0):
            return nums
        
        inflection = k % len(nums)
        a = k % len(nums)

        nums[:] = nums[-a:]+nums[:-a]
        