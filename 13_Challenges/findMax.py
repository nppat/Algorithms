''' 5) Find max '''
# Given an array with multiple values, write a function that returns
# the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)

x = [-3,3,5,7]

def findMax(x):
	maximum = x[0]
	for item in range(len(x)):
		if(x[item] > maximum):
			maximum = x[item]
	print maximum

findMax(x)