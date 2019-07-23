def minAddToMakeValid(S):
    leftOvers = [S[0:1]]
    for character in S[1:]:

        if(len(leftOvers) >0 and  leftOvers[-1] != character ):

            if(character == "(" and leftOvers[-1] == ")"):
                
                leftOvers.append(character)
                continue
            leftOvers.pop()
        else:
            leftOvers.append(character)
    return len(leftOvers)

