class Solution(object):
    def strStr(self, haystack, needle):
        if(len(needle) == 0 or haystack == needle):
            return(0)
        if(len(needle) > len(haystack)):
            return(-1)
        for i in range(len(needle),len(haystack)+1):
            if(haystack[i-len(needle):i] == needle):
                return(i-len(needle))

        return -1
