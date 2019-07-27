def removeOuterParentheses(string):
    # Start and end are used to slice the inner part of a paren.
    start = None
    end = None
    leftstack = []
    validParen = ""
    for character in range(len(string)):
        if(string[character] == "("):
            if(len(leftstack) == 0):
                start = character
            leftstack.append(string[character])
        elif(string[character] == ")"):
            if(len(leftstack) == 1):
                end = character
            leftstack.pop()
        if(start!= None and end != None):
            # concatonates the inner-parts of the paren to the string.
            validParen+= string[start+1:end]
            # Resets the limits of the slice.
            start = None
            end = None
    return validParen
