def find_index(sorted_list, target):
  left = 0
  right = len(sorted_list)-1
  
  while (left <= right):
    middle = (right + left) //2
    if(sorted_list[middle] == target):
      return middle
    elif(target > sorted_list[middle]):
      left = middle+1 
    else:
      right = middle -1

  if(target == middle):
    return middle
  return 0
  