'''
Second-to-Last

Given an array, return the second-to-last element.  

'''

myList = [1,2,3,4,5,6,7,8,9,10]

def returnSecondToLast(a): # define function with one parameter
	print a[len(a) - 2] # print out the 2nd to last element in the list

returnSecondToLast(myList) # call function, pass in myList