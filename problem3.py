'''
Problem 3: What is the largest prime factor of the number 600851475143?
https://projecteuler.net/problem=3
run, from the command line, with python problem3.py 600851475143
	takes hours to execute, for such large values 
'''

import sys

from math import sqrt

def primes_to_sqrt_n(sqrt_n):
	primes = []
	
	'''
	sieve of erastothenes: https://primes.utm.edu/prove/prove2_1.html#trial
	looks at odd numbers only, because even numbers > 2 can't be prime
	'''
	for odd in range(3, sqrt_n + 1, 2):
		print(f'Testing {odd}')
		if not any([odd%prime==0 for prime in primes]):
			primes.append(odd)
			yield odd

def largest_prime_factor_of_n(n):
	sqrt_n = int(sqrt(n))
	
	primes = list(primes_to_sqrt_n(sqrt_n))
	
	spfs = sorted([prime for prime in primes if n%prime==0])
	
	return spfs[-1]

def main(*args):
	n = int(args[0])
	lpf = largest_prime_factor_of_n(n)
	print(f'Largest prime factor of {n}: {lpf}')
	
if __name__ == '__main__':
	main(*sys.argv[1:])