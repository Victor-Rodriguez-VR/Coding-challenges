def da_sort(nums):
    smallestNumber = None
    inOrder = []
    for num in nums:  
        while len(inOrder) >0 and num < inOrder[-1]:
            
            if(smallestNumber is None or num < smallestNumber):
                smallestNumber = inOrder.pop()
            else:
                inOrder.pop()
        inOrder.append(num)
    while(inOrder[-1] > smallestNumber):
        inOrder.pop()
        
    return len(nums) - len(inOrder)
  
print(da_sort([1, 5, 2, 3, 6, 4]))