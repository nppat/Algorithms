'''
Remove Negatives

Implement a function removeNegatives() that accepts an array and
removes any values that are less than zero.

Optional: do this without two nested loops.  

'''

numbers = [1,2,-3,4,-5,10,-20] # list of numbers, negatives included

def removeNegatives(a): # define the function with one argument
	for item in a: # loop through the list passed into a
		if(item < 0): # Check if the item is less than zero
			a.remove(item) # IF less than zero, remove from list
	print(a) # print out new list

removeNegatives(numbers)  # run the funciton