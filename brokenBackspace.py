def k_backspace(inputString):
  stacko = ''
  for character in inputString:
    if(character != "<"):
      stacko+=character
    elif(character == '<' and len(stacko) != 0):
      stacko = stacko[:len(stacko)-1] + stacko[len(stacko)+1:]
  return stacko
	