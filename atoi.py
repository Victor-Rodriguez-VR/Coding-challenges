def atoi(a):
    space = 0
    isNegative = 1
    if(len(a) ==0):
        return 0
    spaces = a.rfind(' ')
    newString = a[spaces+1:]
    if(newString[0].isnumeric() == False and len(newString) == 1):
        return 0
    if(newString[0] == '+'):
        newString = newString[1:]
    if(newString[0] == '-1'):
        newString = newString[1:]
        isNegative = -1
    solution = int(newString)
    if(isNegative == -1):
        solution *=-1
    if (solution > (2 ** 31) - 1):
        return (2 ** 31) - 1
    if (solution < (-2 ** 31)):
        return (-2 ** 31)

    return int(solution)
    print(newString)
print(atoi("+"))
