# dicetoorderedhand(a, b, c) [5pts]
# Write the function dicetoorderedhand(a, b, c) that takes 3 dice and
# returns them in a hand, which is a 3-digit integer. However, even if the
# dice are unordered, the resulting hand must be ordered so that the largest
# die is on the left and smallest die is on the right. For example:
# assert(dicetoorderedhand(1,2,3) == 321)
# assert(dicetoorderedhand(6,5,4) == 654)
# assert(dicetoorderedhand(1,4,2) == 421)
# assert(dicetoorderedhand(6,5,6) == 665)
# assert(dicetoorderedhand(2,2,2) == 222)
# Hint: You can use max(a,b,c) to find the largest of 3 values, and
# min(a,b,c) to find the smallest.

def dicetoorderedhand(a, b, c):
	# your code goes here
	l=[]
	l.append(a)
	l.append(b)
	l.append(c)
	l.sort(reverse=True)

	# s = ' '.join([str(elem) for elem in l])
	s = ""
	# maxi = max(a, b, c)
	# mini = min(a, b, c)
	# s+=str(maxi)+str(mini)
	# l = [a, b, c]
	# r=(l.remove(max(l)))
	# s=str(max(l))+str(r)+str(min(l))
	for i in l:
		s+=i
	return(s)
