# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

def ishappy(n):
	s=str(n)
	if (n < 0):
		return False
	else:
		while len(s) > 1:
			t = 0
			for i in t:
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
			
	# return 0
