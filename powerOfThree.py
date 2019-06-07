def isPowerOfThree(self, n):
        currentNumber = 3
        if(n ==1):
            return True
        while(currentNumber <= n):
            if(currentNumber== n):
                return True
            currentNumber*=3
        return False
        
