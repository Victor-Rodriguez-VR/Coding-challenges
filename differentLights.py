# You are reading a digital signal coming from a light sensor connected to a pin on a microcontroller. Your job is to figure out which light has been turned on based on it's behavior.

# You are given an unsorted list of integers from 0-255 representing the light level during a period of time, where each element is the reading for 1 millisecond of time.

# There is a fair amount of random noise coming in, and a distinct period of time where a light is turned on. If a light is turned on, it will be on for a period of time longer than a few milliseconds - but you're not sure how long.

# Each light has a distinct pattern of lighting up:

# Halogen lights brighten slowly after an initial jump in luminosity, and dim almost instantly, and produce more variation in light emitted
example_one = [4,4,5,5,4,3,3,4,5,77,77,77,78,79,80,81,88,90,95,100,100,110,115,135,145,158,158,190,200,200,200,200,200,150,100,60,7,8,8,8] # halogen


# Florecent lights brighten faster than halogen lights, produce a steadier light than halogen, and dim more slowly.
example_two = [4,5,100,8, 9, 11, 2, 3,4,5,6,5,4,5,4,100,110,115,135,145,158,158,190,7,200,200,200,200,200,200,200,200,190,100,90,87,80,30,25,26,27,28,29,30,30,30,30,30,30,30] # florecent


# Incandecent lights brighten nearly immediately, and dim nearly immediately, and produce a consistent amount of light
example_three = [4,4,5,5,4,3,3,4,100,4,4,5,5,4,3,3,4,5,100,150,200,200,200,201,201,200,201,200,199,200,200,199,201,150,4,4,5,5,4,3,3,4,9,4,4,5,5,4,3,3,4,5,] # incandecent

# LED lights brighten immediately, dim immediately, and produce a brighter amount of consistent light than incandecent lights
example_four = [4,4,5,5,4,3,3,4,100,4,4,5,5,4,3,3,4,5,200,200,200,200,200,200,200,200,200,200,200,200,200,4,4,5,5,4,3,3,4,9,4,4,5,5,4,3,3,4,5,] # LED



# You are also not sure how bright it is in the room to begin with, so you cannot assume there is no light in the room to start. Only that an overhead light is on or off.
# Write a function that returns which kind of light bulb has turned on, as a string (one of "halogen", "florecent", "incandecent", "LED")

## Examples




def light_period(measurements):
  low = []
  on = []
  dim = []
  lowDim = []
  spike = False
  wasOn = True
     
  for character in range(len(measurements)):
    if(spike == False and measurements[character] < 10):
      low.append(measurements[character])
    if(measurements[character] > 60):
      spike = True
      on.append(measurements[character])
  if(len(low) >=5 and len(on)>=20):
    return "halo"
  elif(len(low)<5 and len(on)>=20):
    return "flor"
  elif( len(low) >=5 and len(on)>=15):
    return "Ican"
  else:
    return "led"
  

print(light_period(example_one))
print(light_period(example_two))
print(light_period(example_three))
print(light_period(example_four))
      
    