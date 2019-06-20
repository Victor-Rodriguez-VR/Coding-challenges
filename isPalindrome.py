def isPalindrome(self,s):

    left = 0
    right = len(s) - 1
    while right > left:
        if not s[left].isalnum():
                i += 1
        elif not s[right].isalnum():
            j -= 1
        elif s[left].lower() == s[right].lower():
            i += 1
            j -= 1
        else:
            return False
            
    return True
  
      