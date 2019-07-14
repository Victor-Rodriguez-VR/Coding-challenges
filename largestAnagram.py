class Solution(object):
   def findLongestWord(self, string, dictionary):
      longest = ''
      for anagram in dictionary:

        lastIndex=0
        isCorrect = True
        for letter in range(len(anagram)):

          lastIndex=string.find(anagram[letter] , lastIndex)+1
          if(lastIndex==0):
            isCorrect=False
            break
        if(isCorrect):
          if(len(anagram)>len(longest)):
            longest = anagram
          elif(len(anagram) == len(longest)):
            longest=min(anagram , longest)
          else:
            continue
      return longest