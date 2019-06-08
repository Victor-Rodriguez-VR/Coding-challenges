def isPowerOfThree(self, n):
        ## confirms n is above 3 to be divisible, and 
        ## modded by 3 to mean it is perfectly divisible
        while(n>2 and n%3 !=0):
            n/=3
        ## 1 is the only answer. Even in its simplest form
        ## 3/3 =1
        if(n==1):
            return True
        ## anything else is false.
        return False