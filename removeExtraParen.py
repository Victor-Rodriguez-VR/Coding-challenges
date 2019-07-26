def removeOuterParentheses(string):
    # Creation of left-paren-only stack.
    leftStack = []
    # contains the valid parenthesis.
    validParen = ""
    for character in string:

        if(len(leftStack) >= 1):
            if(character == "("):
                leftStack.append(character)
                
                validParen+= character
            elif(character == ")"):
                if(len(leftStack) == 1):
                    leftStack.pop()
                    continue
                leftStack.pop()
                # adds the character into validParen.
                validParen+= ")"
        else:
            leftStack.append(character)
    return validParen