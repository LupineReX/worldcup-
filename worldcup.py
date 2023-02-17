import random
import sys
import time
#This function allows text to be typed out when you print it 
def type(text):
  words = text
  for char in words:
    time.sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
#this function allows a random choice to be picked from a list
def oppdr(list):
  return random.choice(list)
#this functions allows for everything before this function in the console to be wiped out
def clearConsole():
    print("\033[H\033[J", end="")
#this function returns a random number between 1 and 10
def curv():
 return random.randint(1,10)
# this function allows you to pick an element of a list using an int
def listpicker(list, num):
  return list[num -1]
