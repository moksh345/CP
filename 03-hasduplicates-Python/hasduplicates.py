# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	# Your code goes here
	for i in range(len(L) - 1):
		for j in range(i + 1, len(L)):
			for item in L[i]:
				for t in L[j]:
					if item == t:
						return True
	return False

	# pass