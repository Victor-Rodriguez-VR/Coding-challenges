class Solution(object):
    def reverseString(self, s):
        length = len(s)
        pivot = len(s) //2
        for i in range( pivot):
            temp = s[i]
            s[i] = s[length-1-i]
            s[length-1-i] = temp

            
            

        
