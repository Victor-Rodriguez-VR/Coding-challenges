def sentiment_scores(sentiments, texts):
    # Contains the sentinmentaly scores by the end.
    howSentimental = []
    
    for text in texts:
        # By default all scores start at 0.
        sentimentalScore = 0
        # We seperate every word from one another
        words = text.split(" ")
        # "Words" is one index from texts.
        for word in words:
            # Confirms the last letter isn't puncuation
            if(not word[-1].isalpha()):
                word = word[:len(word)-1]
            # Confirms the word is in sentiments, and acts accordingly.
            if(sentiments.get(word)):
                sentimentalScore += sentiments[word]
            else:
                continue
        # appends the sentimentality score to howSentimental
        howSentimental.append(sentimentalScore)

    # Returns the scores :)
    return howSentimental
  


texts = ["that makes me so happy! amazing.", "I'm so angry about this sad thing.", "sad but true, amazing","yes that is great, and amazing"]


sentiments = {"amazing": 0.4,"sad": -0.8,"great": 0.8,"no": -0.1,"yes": 0.1,"angry": -0.7,"happy": 0.8}
print(sentiment_scores(sentiments,texts))