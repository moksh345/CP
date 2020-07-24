# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	s = str(n)
	print(s)
	if (k < len(s)):
		print(s[k])
		s.replace(s[k],str(d))
		# t = s[::-1]
		# print(t[0])
		# t[k - 1] = d
		# print(t)
		return int(s)
fun_set_kth_digit(1234,1,3)

