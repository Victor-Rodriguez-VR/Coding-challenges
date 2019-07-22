def evaluate_expression(expression):
  answerStack = []
  for currentItem in expression:

      if(currentItem.isdigit() == True):

          answerStack.append(int(currentItem))
      else:
          
          lastDigit = answerStack.pop()
          if(currentItem == '+'):
              answerStack[-1] = answerStack[-1] + lastDigit

          elif(currentItem == '-'):
              answerStack[-1] = answerStack[-1] - lastDigit

          elif(currentItem == '/'):
              answerStack[-1] = int(answerStack[-1] / lastDigit)

          elif(currentItem == '*'):
              answerStack[-1] = answerStack[-1] * lastDigit           

  return answerStack.pop()
