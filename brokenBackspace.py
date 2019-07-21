def k_backspace(inputString):
  stacko = []
  for character in inputString:
    if(character != "<"):
      stacko.append(character)
    elif(character == '<' and len(stacko) != 0):
      stacko.pop()
  return "".join(stacko)
	