# Calculates the number of trailing zeros in n!
def fast_trailing_zero_factorial(n):
  # The only two numbers we could use for this problem would be 2 or 5. We use 5's as it there is less than or equal to the # of 2's in prime factorization. 
  multipleOfFive=1 
  # You would keep dividing by powers of 5 
  while(n>=5*multipleOfFive):
    multipleOfFive+=1 # The number of 5's have increased. 
  return multipleOfFive-1 # Return the number of times you divided by 5 minus 1 since we started at 1 and not zero.
    
    
