# Test!!
def compressSquareImage(image, size):
  # declare final output string number
  size = str(size)
  compressedSquareImage = size + "x" 
  currentLetter = image[0]
  count = 0
  # go through the entire string
  for i in range(len(image)):
    # check which letter we're looking at
    if image[i] != currentLetter:
        compressedSquareImage += currentLetter + str(count)
        # if not, switch the count that we're adding to
        currentLetter = image[i]
        #clear the count of the one we were first adding to 
        count = 0
    # add to the count of that letter   
    count += 1
  compressedSquareImage += currentLetter + str(count)

  return compressedSquareImage
    


