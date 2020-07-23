# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math

def distance(x1, y1, x2, y2):
	d = sqrt((x2 - x1)** 2 + (y2 - y1)** 2)
	
def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	d12 = distance(x1, y1, x2, y2)
	d23 = distance(x2, y2, x3, y3)
	d31 = distance(x1, y1, x3, y3)
	if (math.isclose(d12 ** 2, (d23 ** 2 + d31 ** 2)) or math.isclose(d23 ** 2, (d12 ** 2 + d31 ** 2)) or math.isclose(d31 ** 2, (d23 ** 2 + d12 ** 2))):
		return True
	return False


	# pass
