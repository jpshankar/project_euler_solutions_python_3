'''
Problem 7: What is the 10,001st prime number?
https://projecteuler.net/problem=7
run with python problem7.py 10001
'''

import sys

from itertools import count

#sieve of erastothenes: https://primes.utm.edu/prove/prove2_1.html#trial
def prime_n(n):
	primes = [2]
	
	for odd in count(3, 2):
		if not any([odd%prime==0 for prime in primes]):
			primes.append(odd)
			if len(primes) == n:
				break
				
	return primes[-1]

def main(*args):
	n = int(args[0])
	
	nth_prime = prime_n(n)
	print(f'Prime number no. {n}: {nth_prime}')

if __name__ == '__main__':
	main(*sys.argv[1:])