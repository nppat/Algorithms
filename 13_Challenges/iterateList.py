''' 4) Iterate an array '''
#Write a function that returns the sum of all the values within an
#array. (e.g. [1,2,5] returns 8, [-5,2,5,12] returns 14)

x = [1,2,5]

def iterateList(x):
	result = 0
	for item in x:
		result += item
	print result

iterateList(x)