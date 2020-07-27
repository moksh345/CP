# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	l = len(s)
	if (n > 0):
		if n > l:
			n = n
		n=l-n
		for i in range(n):
			s = s[n:] + s[0:n]
			return s
	elif n < 0:
		for i in range(abs(n)):
			s = s[l - 1] + s[:(l - 1)]
		return s	
	return s

