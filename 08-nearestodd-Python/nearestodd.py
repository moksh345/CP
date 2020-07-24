# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.



def fun_nearestodd(n):
	t = round(n)
	# print(round(16.5))
	if (t % 2 != 0):
		return t
	else:
		if (t < n):
			return t + 1
		elif (t >= n):
			return t-1


