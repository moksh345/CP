"""Implement quick sort in Python.
Input a list.
Output a sorted list. """

def partitn(array, low, high):
	i = low - 1
	pivot = array[high]
	for j in range(low, high):
		if array[j] <= pivot:
			i += 1
			array[i], array[j] = array[j], array[i]
	array[i + 1], array[high] = array[high], array[i + 1]
	return i+1


def quicksort(array):
	# Your code goes here
	low = 0
	high = len(array) - 1
	
	pass