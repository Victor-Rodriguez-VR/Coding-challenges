def minimumCharacters(s):
  count =0
  i = 0
  j = len(s) - 1
  while j > i:
    if not s[i].isalnum():
      i += 1
    elif not s[j].isalnum():
      j -= 1
    elif s[i].lower() == s[j].lower():
      i += 1
      j -= 1
    else:
      count+=1
      j-=1
  return count
 