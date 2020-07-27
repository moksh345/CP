# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.
def isprime(n):
	t = 0
	for i in range(2, (n // 2) + 1):
		if n % i == 0:
			t += 1
	if t <= 0:
		return True
	return False

def fun_hasnoprimes(l):
	for i in l:
		for j in i:
			if isprime(j):
				return False
	return True

