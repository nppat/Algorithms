''' 10) Negatives '''
# Given an array with multiple values, write a function that replaces
# any negative numbers within the array with the value of 0.
#When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])

myList = [1,5,10,-2]

def negatives(x):
	newList = []

	for item in x:
		if item < 0:
			item = 0
		newList.append(item)
	x = newList
	print x

negatives(myList)