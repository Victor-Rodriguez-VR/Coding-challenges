def atoi(a):
  stringlyAnswer = ""
  space = 0
  for n in range(len(a)):
    if(a[n] != " "):
      space = n
      break
    
  if( (a[space].isalpha() == True) and a[space] != "-" and a[space] != "+"):
    return 0
  for ne in range(space, len(a)):
    if(a[ne] != " " and a[ne].isalpha() != True):
      stringlyAnswer+= a[ne]
    else:
      break
  stringlyAnswer = int(stringlyAnswer)
  if(stringlyAnswer > (2**31) -1):
    return (2**31) -1
  if(stringlyAnswer < (-2**31)):
    return (-2**31)
  return stringlyAnswer
  
      