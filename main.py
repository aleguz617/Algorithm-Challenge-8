#Write a function that fixes the error in a pattern in an array.
import random

a = [1,1,2,3,5,8,13,21]

def createError(): #DO NOT CHANGE
	b = random.randint(2,len(a)-1)
	a[b] += random.randint(-4,4)

createError()

def fixError():
  for value in a:
    if value != len(a):
      
  pass

fixError()

print(a)


