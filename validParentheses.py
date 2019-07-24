def valid(parentheses):
    left = "[({"
    right = "])}"
    parenStack = [parentheses[0:1]]

    for character in parentheses[1:]:
        #The left
        if(left.find(character) != -1):
            parenStack.append(character)
        #The right
        else:
            if(len(parenStack) >0):
                lastCharPosition = right.find(character)

                if(lastCharPosition != left.find(parenStack[-1])):
                    return 0

                elif(lastCharPosition == left.find(parenStack[-1])):
                    parenStack.pop()
                    
            else:
                return 0 
    return 1
     

