''' 3) Sum odd 5000 '''
oddSum = 0

for item in range(0,5001):
	if(item % 2 == 1):
		oddSum += item 

print oddSum