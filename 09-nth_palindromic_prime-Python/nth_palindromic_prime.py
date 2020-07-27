# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2

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


def fun_nth_palindromic_prime(n):
	if n == 0:
		return 2
	count = 0
	i = 3
	while (count < n):
		if (isprime(i)) and (str(i) == str(i)[::-1]):
			count = count + 1
			if count == n:
				break
			i += 1
		i += 1
	return i
			
	
	return 0