def backspaceCompare(String1, String2):
    # s1 and s2 are dummies that hold the backspaced strings.
    s1 = ""
    s2 = ""
    # Each dummy uses the same stack.
    characterStack = []
    for character in String1:
        # If the character is not #, adds the character to the stack.
        if(character != "#"):
            characterStack.append(character)
        else:
            # if the character is #, and the stack has is not empty, removes the lastest item inserted.
            if(len(characterStack)>0):
                characterStack.pop()
            # Otherwise does nothing.
    # Collapes the items from the stack into a string.
    s1 = s1.join(characterStack)
    # resets the stack
    characterStack = []
    # repeats lines 7-14 but with the second string.
    for character in String2:
        if(character != "#"):
            characterStack.append(character)
        else:
            if(len(characterStack)>0):
                characterStack.pop()
    s2= s2.join(characterStack)
    
    return s1 == s2
sampleInput1A = "ab#"
sampleInput1B = "ab#"
print(backspaceCompare(sampleInput1A, sampleInput1B))