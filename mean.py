import sys

sum =0
n =0

# Sum input values
file_name = 'data2.txt'

for num in open (file_name):
	sum += float(num)
	n += 1

print sum/n

