# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	# Your code goes here
	l1 = len(str(x))
	l2 = len(str(y))
	t = str(x) + str(x)
	if l1 != l2:
		return False
	if (t.count(str(y)) > 0) or (str(x)[::-1] == str(y)):
		return True
	return False

	# pass