''' 7) Array Odd '''
# Write a function that would return an array of all the odd numbers
# between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.
# myList = list(range(1,51))

def oddNumbers(x):
	oddList = []
	for item in range(len(x)):
		if(item % 2 == 1):
			oddList.append(item)
	print oddList

oddNumbers(myList)