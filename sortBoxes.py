class Solution(object):
    def sortColors(self, nums):
        currentIndex = 0
        lastIndex = len(nums)
        
        while currentIndex < lastIndex:
            if(nums[currentIndex] == 2):
                del nums[currentIndex]
                nums.append(currentIndex)
                lastIndex-=1
                currentIndex-=1

            if(nums[currentIndex] == 0):
                del nums[currentIndex]
                nums.insert(0,0)
            currentIndex+=1