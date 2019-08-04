class Solution(object):
    def isPalindrome(self,theString):
        # Left starts at beginning of the string, right at the end.
        left = 0
        right = len(theString) - 1
        # while right does not pass left
        while right > left:
            # If left is not alphanumeric (numbers or letters)
            if not theString[left].isalnum():
                # Skips the letter
                    left += 1
            # If right is not alphanumeric (numbers or letters)
            elif not theString[right].isalnum():
                # Skips the letter.
                right -= 1
            # By  now left and right can only be alphanumeric.
            # If they are equal to one another, continues.
            elif theString[left].lower() == theString[right].lower():
                left += 1
                right -= 1
            # If all else fails, it is not palindrome.
            else:
                return False
        # When loop finishes, true. 
        return True
  