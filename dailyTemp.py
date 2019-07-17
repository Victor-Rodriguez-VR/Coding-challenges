def dailyTemperatures(dailyTemps):
  #Given a list of daily temperatures, return the number of days till a raise in temperature is found.
  theOutput = [0] * len(dailyTemps)
  stack = []
  for index in range(len(dailyTemps)):
    temp = dailyTemps[index]
    while len(stack) >0 and temp > dailyTemps[stack[-1]]:
      lastHotDay = stack.pop()
      theOutput[lastHotDay] = index - lastHotDay
    stack.append(index)
  return theOutput

sampleInput = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(sampleInput))