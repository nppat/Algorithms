from __future__ import division
# This from __future__ import division makes Python division act normal,
#not using this takes the result and rounds down for some reason.

''' 11) Max/Min/Avg '''
#Given an array with multiple values, write a function that returns a new array
#that only contains the maximum, minimum, and average values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5])

myList = [1,5,10,-2]

def maxMinAvg(x):
	maximum = 0
	minimum = 0
	result = 0

	for item in x:
		if item > maximum:
			maximum = item
		if item < minimum:
			minimum = item
		result += item 

	average = result / len(x)
	print maximum, minimum, average

maxMinAvg(myList)