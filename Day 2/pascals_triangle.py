#generate pascal's triangle
number_of_rows=int(input('Please enter a number of rows (at least 2): '))
pascals_triangle=[[1],[1,1]]
for extra_rows in range(number_of_rows-2):
	previous_row=pascals_triangle[-1]
	new_row=[]
	new_row.append(1)
	for index in range(len(previous_row)-1):
		new_row.append(previous_row[index]+previous_row[index+1])
	new_row.append(1)
	pascals_triangle.append(new_row)

#print it nicely
total_rows=len(pascals_triangle)
for row in range(total_rows):
	row_start_space=total_rows-1-row
	row_string=row_start_space*'\t'
	for number in pascals_triangle[row]:
		row_string+=(str(number)+'\t\t')
	print(row_string)
	
