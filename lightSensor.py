# You are reading a digital signal coming from a light sensor connected to a pin on a microcontroller.
# You are given an unsorted list of integers from 0-255 representing the light level during a period of time, where each element is the reading for 1 millisecond of time.

# There is a fair amount of random noise coming in, and a distinct period of time where a *halogen* light is turned on. If a light is turned on, it will be on for a period of time longer than a few milliseconds - but you're not sure how long.


# You are also not sure how bright it is in the room to begin with, so you cannot assume there is no light in the room to start. Only that an overhead light is on or off.
# Write a function that returns the length of time the light is on, in milliseconds.


## Examples
example_one = [4,4,5,5,4,3,3,4,5,77,77,77,78,79,80,81,88,90,95,100,100,110,115,135,145,158,158,190,200,200,200,200,200, 7,8,8,8] # 24ms (dark room to dim room)

example_two = [4,5,100,8, 9, 11, 2, 3,4,5,6,5,4,5,4,100,110,115,135,145,158,158,190,7,200,200,200,200,7,8,8,8,4,5,11,2,12,24,25,26,27,28,29,30,30,30,30,30,30,30] # 14ms (dark room to bright room)

example_three = [40,50,100,80, 90, 110, 20, 30,40,50,60,50,40,50,40,200,210,215,235,245,250,250,230,240,200,200,200,190,190,200,150,70,80,80,80,40,50,110,20,120,40,25,26,27,28,29,30,30,30,30,30,31,30] # 15ms (dim room to bright room)

#Split array into 3 sections: Dark, light is on, dark
#Light will be on when values increase considerably for a consistent
#number of values
#Light will be turned off when it starts and when values spike down, relative to values of light being on

#Issue: How to eliminate/identify noise???
#Take a current avg for a set of values, if consistent its valid



def light_period(measurements):
  smallStack = list()
  smallStack.append(measurements[0])
  largeStack = list()  
  for light in range(1,len(measurements)):
    temp = measurements[light]
    smallie = smallStack[-1]
    if( len(str(temp)) <= len(str(smallie))):
      smallStack.append(temp)
      if(len(largeStack ) ==1):
        largeStack.pop()
    elif(len(str(temp)) > len(str(smallie)) ):
      largeStack.append(temp)
  return largeStack
  
 
print(len(light_period(example_three)))