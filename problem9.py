'''
problem 9: There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
https://projecteuler.net/problem=9
run with python problem9.py 1000
'''

import argparse

from itertools import accumulate, count
from operator import mul

parser = argparse.ArgumentParser()
parser.add_argument('num', nargs='?', type=int)

'''
'''

def generate_pythagorean_triples(triple_list, num):
	'''
	uses Dickson's method to generate triples: https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#Dickson's_method
		generates all triples for r values where r^2 <= num 
	'''
	for r in count(2):
		_r = r
		if _r**2 <= num:
			st = (_r**2)//2
			factor_pairs = [(n, st//n) for n in range(2, st) if st%n==0]
			for s, t in factor_pairs:
				triple_list.append((_r + s, _r + t, _r + s + t))
		else:
			break	
			
def main(num):
	triple_list = []
	generate_pythagorean_triples(triple_list, num)
	for py_triple in triple_list:
		print(py_triple)
		tri_sum = sum(py_triple)
		#if the sum of the triple is a factor of num, we can use it to get the triple that sums up to num
		if num%tri_sum==0:
			#tuple->list here because of bug where itertools.accumulate returns an empty list for a tuple
			num_triple = [int(py_tp * (num/tri_sum)) for py_tp in py_triple]
			#shows that the triple's values sum up to num
			num_tri_str = ' + '.join([str(nt) for nt in num_triple])
			print(f'{num_tri_str} = {num}')
			
			#outputs the product of the triple
			tri_prod = list(accumulate(num_triple, mul))[-1]
			print(f'Product of above terms: {tri_prod}')
			break
			
if __name__ == '__main__':
	args = parser.parse_args()
	main(args.num)