class Solution(object):
    def lengthOfLastWord(self, s):
        wordLen = 0
        index = len(s) - 1
        while(index >= 0 and s[index] == ' '):
            index -= 1
        while index >= 0 and s[index] != ' ':
            wordLen += 1
            index -= 1
        return wordLen