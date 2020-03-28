class Solution(object):
    def findPairs(self, nums, k):
        count = 0 
        c = collections.Counter(nums) #Counter is vital for this efficient runtime.
        # Counter makes a hasmap that keeps track of occurances. 
        for i in c:
        ## j-i = k, which means k+i= j. If k+i within C, then that means we found a pair.
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                count += 1
        return count
