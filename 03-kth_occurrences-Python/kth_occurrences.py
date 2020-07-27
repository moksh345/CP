# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	s = s.strip()
	li = list(s)
	freq = {}
	for item in li:
		if item in freq:
			freq[item] += 1
		else:
			freq[item] = 1
			x = []
	l = list(freq.values())
	m = list(freq.keys())
	l.sort(reverse=True)
	p = list(freq.values())
	for i in l:
		t=m[p.index(i)]
	return 'a'


