from __future__ import division
# This from __future__ import division makes Python division act normal,
#not using this takes the result and rounds down for some reason.

''' 6) Find average '''
#Given an array with multiple values,
#write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)

x = [1,3,5,7,20]

def findAverage(x):
	result = 0
	for item in x:
		result += item
	average = result / len(x)
	return average

av = findAverage(x)
print av
