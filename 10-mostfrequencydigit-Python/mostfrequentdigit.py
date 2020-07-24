# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.
from collections import Counter
def count(x,d):
	count = 0
	while (x):
		if (x % 10 == d):
			count += 1
		x = x // 10
	return count
		

def mostfrequentdigit(n):
	# your code goes here
	# s = str(n)
	# # counter creates dictionary which will have strings as key and their frequencies as value 
	# d = Counter(s)
	# maxi = max(d.values())
	# i = d.values().index(maxi)
	# return d.items()[i]
	max=1
	for d in range(10):
		c = count(n, d)
		if (c > max):
			max = c
			res = d
	return res
	