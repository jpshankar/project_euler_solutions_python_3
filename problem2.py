'''
Problem 2: Find the sum of all even Fibonacci numbers under four million.
https://projecteuler.net/problem=2
run, from the command line, with python problem2.py 4000000
'''

import sys

def generate_fibonacci_up_to_n(fibonacci, n):
	next_term = fibonacci[-1] + fibonacci[-2]
	if next_term < n:
		fibonacci.append(next_term)
		generate_fibonacci_up_to_n(fibonacci, n)

def sum_even_valued_fibonacci_nums_under_n(n):
	fibonacci = [1, 2]
	
	generate_fibonacci_up_to_n(fibonacci, n)
	
	return sum([f_term for f_term in fibonacci if f_term%2==0])
	
def main(*args):
	n = int(args[0])
	even_sum = sum_even_valued_fibonacci_nums_under_n(n)
	print(f'Sum of even-valued numbers under {n}: {even_sum}')

if __name__ == '__main__':
	main(*sys.argv[1:])