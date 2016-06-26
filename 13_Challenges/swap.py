''' 12) Swap Values '''
# Write a function that will swap the first and last values of any given array.
# The default minimum length of the array is 2. (e.g. [1,5,10,-2] will become [-2,5,10,1]).

myList = [1,5,10,-2]

def swap(x):
	x[0], x[len(x) - 1] = x[len(x) - 1], x[0]
	print x

swap(myList)