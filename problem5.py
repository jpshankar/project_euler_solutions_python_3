'''
problem 5: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
https://projecteuler.net/problem=5
run, from the command line, with python problem5.py 1 20
'''

import math, sys

from itertools import accumulate

from operator import mul

def sieve_from_m_to_n(m, n):
	'''
	sieve of erastothenes from m to n, looking only at odd numbers > 2
	'''
	primes = []
	if m <= 2 and m > 0:
		yield 2
		primes.append(2)
		
	if n > 3:
		for odd in range(3, n+1, 2):
			if not any([odd%prime==0 for prime in primes]):
				primes.append(odd)
				yield odd
	elif n==3:
		yield 3
		
def get_prime_factors_of_i(i, primes, factors):
	_i = i
	if i > 1:
		#for each prime..
		for p in primes:
			#.. if the prime is a factor of _i
			if _i%p == 0:
				#..and if the prime hasn't been determined as a factor
				if p not in factors:
					#..divide all the occurences of that prime out, adding each as a factor
					while _i%p==0:
						_i//=p
						factors.append(p)
				#..or if _i is non-prime and still needs to have 2 divided out of it
				elif _i%2==0:
					while _i//2!=2 and _i%2==0:
						_i//=2
					if _i%2==0 and _i not in factors:
						factors.append(_i)
				#..work with _i accordingly
				
				#..if, after that, _i is a prime number that hasn't been added as a factor
				if _i in primes and _i not in factors:
					#..add _i as a factor
					factors.append(_i)
	
def main(*args):
	m, n = int(args[0]), int(args[1])
	primes_from_m_to_n = list(sieve_from_m_to_n(m, n))
	
	factor_list = []
	for i in range(n, m-1,-1):
		get_prime_factors_of_i(i, primes_from_m_to_n, factor_list)
	
	factor_prod = list(accumulate(factor_list, mul))[-1]
	print(f'Minimum product from {m}, {n} is {factor_prod}')

if __name__ == '__main__':
	main(*sys.argv[1:]) 