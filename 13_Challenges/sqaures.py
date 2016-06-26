import random

''' 9) Squares '''
# Given an array with multiple values, write a function that replaces each value in the array
# with the product of the original value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])

x = list(random.sample(range(0,100),100)) # this creates a random sample of 100 integers from 0-100 in the list

def squares(x):
	newList	= []
	for item in x:
		newList.append(item**2)
	print newList, '\n' # prints the newList of squares, inserts a new line
	print len(newList) # prints off the number of values in the newList, which should = 100

squares(x)