class Solution(object):
    def isValid(self, s):
        
        left = "[({"
        right = "])}"
        if(len(s) == 0):
            return True
        parenStack = [s[0:1]] # Creates a stack with
        for character in s[1:]:
            #The left
            if(left.find(character) != -1):
                parenStack.append(character)
            #The right
            else:
                if(len(parenStack) >0):
                    lastCharPosition = right.find(character)

                    if(lastCharPosition != left.find(parenStack[-1])):
                        return False

                    elif(lastCharPosition == left.find(parenStack[-1])):
                        parenStack.pop()

                else:
                    return False 
        
        if len(parenStack) != 0:
            return False

        return True
