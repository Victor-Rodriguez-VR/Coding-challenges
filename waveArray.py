def wave_array(integers):
  temp = 0
  for i in range(len(integers)-1):
    if(i%2 == 0):
      if(integers[i] < integers[i+1]):
        temp = integers[i+1]
        integers[i+1] = integers[i]
        integers[i] = temp
    else:
      if(integers[i] > integers[i+1]):
        temp = integers[i+1]
        integers[i+1] = integers[i]
        integers[i] = temp
  return integers
      