# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	# your code goes here
	l = len(a)
	a.sort()
	index=l//2
	print (a)
	if l == 0:
		return 0
	elif l % 2 != 0:
		
		return (a[index] + a[index - 1]) / 2
	return a[index]
	