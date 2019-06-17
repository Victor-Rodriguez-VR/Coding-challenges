def solve(self, A):
    trueAnswer= []
    temp = [1,1]
    dummy = temp[:]
    if(A ==0):
        return trueAnswer
    trueAnswer.append([1])
    if(A>=2):
        trueAnswer.append([1,1])
    i = 2
    while(i < A):
        for n in range (0,len(temp)-1):
            dummy[n+1] = temp[n+1] + temp[n]
        dummy.append(1)  
        temp = dummy[:]
        trueAnswer.append(temp)
        i+=1
    return trueAnswer