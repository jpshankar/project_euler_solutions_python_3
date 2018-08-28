'''
problem 4: What is the largest palindrome made from the product of two 3-digit numbers?
https://projecteuler.net/problem=4
run, from the command line, with python problem4.py 3
	calculates, for all combinations of all three-digit numbers (iterated over from max to min), their products
		checks if they're palindromes through string comparison
	when finished, sorts the list of palindrome products in aescending order and returns the largest
'''

import sys

def largest_palindrome_of_num_digits(num_digits):
	min_factor, max_factor = 10**(num_digits-1), (10**num_digits) - 1
	palindromes=set()
	for fac1 in range(max_factor, min_factor-1, -1):
		for fac2 in range(max_factor, min_factor-1, -1):
			product = fac1 * fac2
			prod_str = str(product)
			prod_str_len = len(prod_str)
			
			#calculate the length of a half of the product string
			hlf_slc = prod_str_len//2
			if prod_str_len%2!=0:
				#account for the product string being non-even length
				hlf_slc+=1
			
			#compare the first half of the string to the second half, reversed- if they're equal, the product's a palindrome
			front_half, back_half = prod_str[0:hlf_slc], prod_str[prod_str_len-1:hlf_slc-1:-1]
			if front_half == back_half:
				palindromes.add(product)
	
	return sorted(palindromes)[-1]
				
def main(*args):
	num_digits = int(args[0])
	if num_digits > 1:
		lp = largest_palindrome_of_num_digits(num_digits)
		print(f'Largest palindrome of {num_digits} digits: {lp}')
	else:
		print(f'Can\'t have a palindrome of {num_digits} digits')

if __name__ == '__main__':
	main(*sys.argv[1:])