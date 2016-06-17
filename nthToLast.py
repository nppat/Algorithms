'''
Nth-to-Last

Return the element that is N-from-array's-end.  
'''

myList = list(range(0,1000)) # create a list with a range of 0 - 1000

def nthToLast(a,n): # define a function with 2 arguments
	print a[len(a) - n] # print out the result

nthToLast(myList,500) # call the function and pass in the arguments

'''
In this case the result would be 500.  n can be changed to any number 0-1000
'''