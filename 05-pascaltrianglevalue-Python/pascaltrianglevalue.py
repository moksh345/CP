# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 




def fun_pascaltrianglevalue(row, col):
	if (row == col or col == 0 or row == 0):
		return 1
	if (col > row):
		return 0
	else:
		return fun_pascaltrianglevalue(row-1,col-1)+fun_pascaltrianglevalue(row-1,col)
	