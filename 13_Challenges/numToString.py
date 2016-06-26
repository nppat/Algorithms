''' 13) Numbers to string '''
# Write a function that takes an array of numbers and replaces any negative values
# within the array with the string 'Dojo'. For example if array = [-1,-3,2], your function will return ['Dojo','Dojo',2].

myList = [-1,-3,2]

def numToString(x):
	newList = []
	for item in x:
		if item < 0:
			item = 'Dojo'
		newList.append(item)
	x = newList
	print x

numToString(myList)