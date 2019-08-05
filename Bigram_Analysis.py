def bigram_frequency_analyzer(text):
    # Ignores the last character if it is empty.
    if(text[-1] == " "):
        text = text[:len(text)-1]
    theDict = dict()
    # Seperates words from one another.
    indivisualWords = text.split(" ")
    # Since we want 2 words, we increment by two.
    for index in range(2,len(indivisualWords),1):
        # The past two words.
        twoWords = indivisualWords[index-2] + " " + indivisualWords[index-1]
        currentWord = indivisualWords[index]
        # Determines if the two words are within the dictionary. Incriments the key's value, or creates a value for the key.
        if(theDict.get(twoWords)):
            if(theDict[twoWords].get(currentWord)):
                theDict[twoWords][currentWord]+=1
            else:
                theDict[twoWords][currentWord] = 1
        else:
            theDict[twoWords] = { currentWord : 1}
    # Creates value to contain all words and their associated values.
    wordsAndNumbers = ""
    for key in theDict:
        # Concatonates the starting key with a colon.
        wordsAndNumbers+= key + " : "
        # Gathers all values from the first key.
        nestedDictionary = theDict.get(key)
        for nestedKey in nestedDictionary:
            # Concatenates the nested keys with their associated value.
            wordsAndNumbers+= nestedKey + " ("+str(theDict[key].get(nestedKey)) +") "
        wordsAndNumbers+="\n"
    return wordsAndNumbers

