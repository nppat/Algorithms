''' 8) Greater than Y '''
#Given value of Y, write a function that takes an array and returns the number of values
#that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2.
#(There are two values in the array greater than 3, which are 5, 7).

x = [1,3,5,7]

def greaterThanY(x,y):
	newList = []
	for item in x:
		if(item > y):
			newList.append(item)
	print len(newList)

greaterThanY(x,2)  # by having y = 2, the function determines there are 3 values greater than 2 in the list (3,5,7)