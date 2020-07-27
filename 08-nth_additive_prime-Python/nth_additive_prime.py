# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def isprime(n):
	if(n == 1):
		return True
	i = 1
	count = 0
	while(i <= n):
		if(n%i == 0):
			count = count + 1
		i = i + 1
	if(count == 2):
		return True
	else:
		return False
	
def isadditive(n):
	s = str(n)
	sum = 0
	for i in s:
		sum += int(i)
	if (isprime(sum)):
		return True
	return False


def fun_nth_additive_prime(n):
	if n == 0:
		return 2
	i = 3
	count = 0
	while (count < n):
		if (isprime(i) and isadditive(i)):
			count += 1
			if count == n:
				break
			i+=1
		i+=1		
	return i