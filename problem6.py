'''
problem 6: 
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
https://projecteuler.net/problem=6
run with python problem6.py 100
'''

import sys

def sum_of_squares_up_to_n(n):
	return sum([i**2 for i in range(1, n+1)])
	
def square_of_sum_of_numbers_up_to_n(n):
	return sum([i for i in range(1, n+1)])**2
	
def main(*args):
	n = int(args[0])
	
	if n >=0:
		square_diff = square_of_sum_of_numbers_up_to_n(n) - sum_of_squares_up_to_n(n)
		print(f'Difference of square of sum of natural numbers up to {n} and sum of natural number squares up to {n}: {square_diff}')
	else:
		print(f'Can only look at values going up to a natural number, which {n} isn\'t')
	
if __name__ == '__main__':
	main(*sys.argv[1:])