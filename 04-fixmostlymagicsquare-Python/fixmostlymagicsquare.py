# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.
def ismostlymagicsquare(a):
	# Your code goes here
	d1 = 0
	d2 = 0
	l = []
	for col in range(len(a)):
		l.append(sum(row[col]for row in a))
	for i in range(0,len(a)):
		s=0
		for j in range(0, len(a[0])):
			if i == j:
				d1 += a[i][j]
			if i == len(a[0]) - j - 1:
				d2 += a[i][j]
			s += a[i][j]
		l.append(s)
	l.append(d1)
	l.append(d2)
	return l
	
def freq(l):
	return max(set(l),key=l.count)

def fixmostlymagicsquare(L):
	k = ismostlymagicsquare(L)
	if len(set(k)) == 1:
		return L
	else:
		x = freq(k)
		for item in set(k):
			if item != x:
				y = item
		diff = x - y
		for i in range(len(L)):
			for j in range(len(L[0])):
				a = L[i][j]
				L[i][j] += diff
				t = ismostlymagicsquare(L)
				if len(set(t)) == 1:
					b = L
					break
				else:
					L[i][j]=a
		return b

	# pass
	# Your code goes here