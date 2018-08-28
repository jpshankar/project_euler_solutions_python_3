'''
problem 8: Find the thirteen adjacent digits in <the given 1000-digit number> that have the greatest product. What is the value of this product?
https://projecteuler.net/problem=8
run with python problem8.py 13 -fWv data/problem8.txt
	-rV allows you to specify the source number directly in the command line
'''

import argparse

from itertools import accumulate
from operator import mul

parser = argparse.ArgumentParser()
parser.add_argument('num', nargs='?', type=int)
parser.add_argument('-rV', nargs='?', type=str)
parser.add_argument('-fWv', nargs='?', type=argparse.FileType('r'))

def main(val, num):
	prod_list = []
	sub_start, sub_end = 0, num
	
	#iterates over all sub-sequences of the number of size num, calculating their products
	while sub_start < len(val):
		sub_str = val[sub_start:sub_end]
		#if 0's in the subsequence, no point in calculating the product
		if not '0' in sub_str:
			prod_list.append(
				list(accumulate([int(digit) for digit in sub_str], mul))[-1]
			)
		sub_start+=1
		sub_end+=1
			
	#sorts products, returns the largest
	largest_product = sorted(prod_list)[-1]
	print(f'Largest product of {num} digits in {val}: {largest_product}')

if __name__ == '__main__':
	args = parser.parse_args()
	if args.rV:
		main(args.rV, args.num)
	elif args.fWv:
		fVal = args.fWv.read().replace('\n', '')
		print(fVal)
		main(fVal, args.num)
	else:
		print(f'Need a value/file containing one')