def backspaceCompare(String1, String2):
    words = [String1, String2]
    # Creates space to store backspaced words.
    backspaced = ["",""]
    stacky = []
    for word in range(len(words)):
        currentWord = words[word]
        for character in currentWord:
            if(character != "#"):
                stacky.append(character)
            else:
                if(len(stacky)>0):
                    stacky.pop()
        backspaced[word] = backspaced[word].join(stacky)
        stacky = []
        
    return backspaced[0] == backspaced[1]
sampleInput1A = "ab#"
sampleInput1B = "ab#"
print(backspaceCompare(sampleInput1A, sampleInput1B))