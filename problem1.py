'''
Problem 1: Find the sum of all multiples of 3 or 5 below 1000.
https://projecteuler.net/problem=1
run, from the command line, with python problem1.py 1000
'''

import sys

def sum_multiples_of_three_and_five(below):
	multiples = [number for number in range(1, below) if number%3==0 or number%5==0]
	return sum(multiples)

def main(*args):
	below = int(args[0])
	below_sum = sum_multiples_of_three_and_five(below)
	print(f'Sum of multiples of three and five below {below}: {below_sum}')

if __name__ == '__main__':
	main(*sys.argv[1:])