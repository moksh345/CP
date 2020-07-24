# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	t = n % 10
	n = int(n / 10)
	while (n):
		pres_digit = n % 10
		if (pres_digit == t):
			return True
		t = pres_digit
		n = int(n / 10)
	return False