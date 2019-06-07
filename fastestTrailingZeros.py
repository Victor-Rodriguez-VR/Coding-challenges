def fast_trailing_zero_factorial(n):
  multipleOfFive=1
  while(n>=5*multipleOfFive):
    multipleOfFive+=1
  return multipleOfFive-1
    
    