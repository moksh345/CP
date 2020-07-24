# ishappynumber(n) [10 pts]
# A happy number is a number defined by the following process: Starting with any positive integer, replace the 
# number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will 
# stay ), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 
# are happy numbers.

# Write the function ishappynumber(n) which takes a possibly-negative integer and returns True if it is happy and 
# False otherwise. Note that all numbers less than 1 are not happy. Here are some test assertions for you:
# assert(ishappynumber(-7) == False)
# assert(ishappynumber(1) == True)
# assert(ishappynumber(2) == False)
# assert(ishappynumber(97) == True)
# assert(ishappynumber(98) == False)
# assert(ishappynumber(404) == True)
# assert(ishappynumber(405) == False)

def ishappynumber(n):
	# your code goes here
	# rem = 0
	# t=0
	
	# else:
	# 	while (n > 0):
	# 		rem = n % 10
	# 		t = t + (rem * 2)
	# 		n = n // 10
	s = str(n)
	if (n == 1):
		return True
	if (len(s)==1 or n < 0):
		return False
	else:
		while (len(s) > 1):
			t = 0
			for item in s:
				t += ((int(item))** 2)
			s = str(t)
		if (int(s) ==1):
			return True
		return False



	pass