# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	#Your code goes here
	l1 = len(str1)
	l2 = len(str2)
	t = str1 + str1
	if l1 != l2:
		return False
	if (t.count(str2) > 0):
		return True
	return False