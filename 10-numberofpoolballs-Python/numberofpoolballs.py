# numberOfPoolBalls(rows) [10pts]
# Pool balls are arranged in rows where the first row contains 1 pool ball and each row contains 1
# more pool ball than the previous row. Thus, for example, 3 rows contain 6 total pool balls
# (1+2+3) . With this in mind, write the function numberOfPoolBalls(rows) that takes a 
# non-negative int value, the number of rows, and returns another int value, the number of pool
# balls in that number  of full rows. For example, numberOfPoolBalls(3) returns 6. We will not 
# limit our analysis to a "rack" of 15 balls. Rather, our pool table can contain an unlimited 
# number of rows. For this problem and the next, you should research Triangular Numbers.

def numberofpoolballs(rows):
	# Your code goes here
	# The formula states (n(n+1))/(2) or (n^(2)+n)/(2) to get a triangular number for given number of rows.
	t=((rows**2)+rows)/2
	return t