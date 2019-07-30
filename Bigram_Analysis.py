def bigram_frequency_analyzer(text):
    theDict = dict()
    # Seperates words from one another.
    indivisualWords = text.split(" ")
    # Since we want 2 words, we increment by two.
    for words in range(2,len(indivisualWords),1):
        # The past two words.
        twoWords = indivisualWords[words-2] + " " + indivisualWords[words-1]
        currentWord = indivisualWords[words]
        if (theDict.get(twoWords)):
            if(theDict[twoWords].get(currentWord)):
                theDict[twoWords][currentWord]+=1
            else:
                theDict[twoWords][currentWord] = 1
        else:
            theDict[twoWords] = { currentWord : 1}
    return theDict