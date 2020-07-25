# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).
def ishappy(n):
	s=str(n)
	if (n < 0):
		return False
	else:
		while len(s) > 1:
			t = 0
			for i in s:
				t += ((int(i))** 2)
			s = str(t)
		if int(s) == 1:
			return True
		return False

def fun_nth_happy_number(n):
	if n==0:
		return 1
	elif n == 1:
		return 7
	i = 2
	count = 1
	while (count <= n):
		if ishappy(i) == True:
			count += 1
			if count == n:
				return i
		i += 1


def fun_nth_happy_prime(n):
	
	return 0