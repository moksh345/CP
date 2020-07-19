# Write the function getInRange(x, bound1, bound2) which takes 3 int values
# x, bound1, and bound2, where bound1 is not necessarily less than bound2. 
# If x is between the two bounds, just return it unmodified. Otherwise, 
# if x is less than the lower bound, return the lower bound, 
# or if x is greater than the upper bound, return the upper bound.

def fun_getinrange(x, bound1, bound2):
	# your code goes here
	if (bound1 > bound2):
		max = bound1
		min = bound2
	else:
		max = bound2
		min = bound1
	if (min < x < max):
		return x
	elif (x < max):
		return min
	else:
		return max
