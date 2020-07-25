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

# def fun_nth_happy_number(n):
# 	if n==0:
# 		return 1
# 	elif n == 1:
# 		return 7
# 	i = 2
# 	count = 1
# 	while (count <= n):
# 		if ishappy(i) == True:
# 			count += 1
# 			if count == n:
# 				return i
# 		i += 1
def isprime(n):
	t = 0
	for i in range(2, (n // 2) + 1):
		if n % i == 0:
			t += 1
	if k <= 0:
		return True
	return False

def fun_nth_happy_prime(n):
	if n == 0:
		return 7
	i = 8
	count = 0
	while (count <= n):
		if (ishappy(i) == True and isprime(i) == True):
			count += 1
			if count == n:
				return i
		i += 1
		
	# return 0