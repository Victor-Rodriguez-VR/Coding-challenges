##Given an unsorted integer array, find the first missing positive integer.



##Example:
##Given [1,2,0] return 3,
##[3,4,-1,1] return 2,
##[-8, -7, -6] returns 1
##Your algorithm should run in O(n) time and use constant space.


def first_missing_positive_integer(integers):
  goodList = []

  
  for position in integers:
    if(position <0 ):
      continue
    elif( position+1 > len(goodList)):
      goodList.extend([False]*(position-len(goodList) +1))
      
    goodList[position]= True
    
  index = 0
  for i in range(1,len(goodList)):
    if(goodList[i] == False):
      return i
      
  if(index ==0 and len(goodList) == 0):
      return 1
  elif (index ==0 and len(goodList) >0):
      return len(goodList)
      
