def count_words(text):
  characterCounter = dict()
  # String to concatonate all words and frequencies.
  stats = ""
  # seperates different words.
  splitText = text.split(" ")
  for token in splitText:
    # removes unnecessary puncuation.
    token = token.lower().replace(".","").replace(",","")
    if(characterCounter.get(token)):
      # increase count for the word.
      characterCounter[token]+=1
    else:
      characterCounter[token] = 1
  for word,count in characterCounter.items():
    #concatonates word and frequency.
    stats+= word +" " + str(count) + " "
  # returns all words with their associated frequencies.
  return stats
 