def removeDuplicates(self, numbers):
    if(len(numbers) ==0):
        return 0
    if(len(numbers) == 1):
        return 1
    for currentIndex in range(len(numbers)-1,0,-1):
        if numbers[currentIndex] == numbers[currentIndex-1]:
            del numbers[currentIndex]
    return len(numbers)
    