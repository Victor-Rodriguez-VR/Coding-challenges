class Solution(object):
    def sortColors(self, nums):
         
        tempBoy = None
        for n in range(len(nums)-1,0,-1 ):
            if(nums[n] == 2):
                del nums[n]
                nums.append(2)
            if(nums[n] == 0 and nums[n-1] == 1):
                tempBoy = nums[n-1]
                nums[n-1] = nums[n]
                nums[n] = tempBoy
        
            
        if(nums[0] == 2):
            del nums[0]
            nums.append(2)
    