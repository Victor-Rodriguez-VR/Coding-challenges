class Solution(object):
    def intersect(self, nums1, nums2):
        possibleRepeats = {} # Our occurance tracker.
        solution = [] # Our intersection of both arrays.
        if len(nums1)<len(nums2): # Larger dictionary, less work to iterate through.
            nums1,nums2 = nums2,nums1
        for i in nums1:
            if i not in possibleRepeats: # Creates occurance in dictionary.
                possibleRepeats[i] = 1
            else:                        # Otherwise increments value in hashmap.
                possibleRepeats[i]+=1
        for i in nums2:
            if i in possibleRepeats and possibleRepeats[i] > 0: # If I is a key in possibleRepeats and the number of occurances is not 0 (decreases for every match in nums2)
                possibleRepeats[i]-=1
                solution.append(i) # decrease occurances of that number and add the key to solution.
        return solution
            
