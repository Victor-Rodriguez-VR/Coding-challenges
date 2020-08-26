class Solution(object):
    def isValid(self, s):
        left = "[({"
        right = "])}"
        if(len(s) == 0):
            return True
        parenStack = [s[0:1]] # Creates a of 
        for character in s[1:]:
            # If the character is in the left, appends
            if(left.find(character) != -1):
                parenStack.append(character)
            else:
                if(len(parenStack) >0):
                    lastCharPosition = right.find(character)
                    # If the leftcharacter's index does not match up with the right's, they're not the same symbol. 
                    if(lastCharPosition != left.find(parenStack[-1])):
                        return False
                    # Otherwise you pop the top item
                    elif(lastCharPosition == left.find(parenStack[-1])):
                        parenStack.pop()
                # If its a right character and no items are left: the parentheses are not valid.
                else:
                    return False 
        # if the stack not size 0, then an item is left and is imbalanced. 
        if len(parenStack) != 0:
            return False
        
        return True
