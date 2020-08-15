class Solution(object):
    def reverseString(self, s):
        length = len(s) 
        pivot = len(s) //2 # The center of the list/string
        for i in range(pivot): # We iterate through half of the list/string
            temp = s[i]
            s[i] = s[length-1-i] # Swap farthest and closest based on i.
            s[length-1-i] = temp 
            
            

        
