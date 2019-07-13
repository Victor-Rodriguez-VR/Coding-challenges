def longest_anagram(s, d):
  
  longest = ''
  isCorrect = None
  for anagram in d:
    isCorrect = None
    dummy = s
    
    for letter in anagram:
      findMe = dummy.find(letter)
      if(findMe != -1):
          dummy  = dummy.replace(letter, "",1)
      else:
          isCorrect = False
          break
    if(isCorrect != False and len(longest) < len(anagram)):
      
      longest = anagram
  return longest
  
 