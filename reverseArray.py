'''
Reverse Array

Given a numerical array, reverse the order of the values.
The reversed array should have the same length, with existing
elements moved to other indices so that the order of elements is reversed. 
'''
myList = [1,2,3,4,5,6,7,8,9,10] # Create a list

def reverseList(a):	# define a function with one argument
	new_list = a[::-1] #create a new variable that takes the argument that is passed and reverses by slicing -1, thus in reverse
	print new_list # print the new_list variable

reverseList(myList) # call the function with the argument myList