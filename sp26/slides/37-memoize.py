from timeit import timeit

num = 20

def fib(n):
	if n < 2:
		return n
	else:
		return fib(n - 1) + fib(n - 2)

print(f"           fib({num})={fib(num)} in {timeit(lambda:fib(num), number=1):.8f}s")

def fib_iter(n):
	last = 1
	prev = 0
	for i in range(1,n):
		next = prev + last
		prev = last
		last = next
	return last

print(f"      fib_iter({num})={fib_iter(num)} in {timeit(lambda:fib_iter(num), number=1):.8f}s")
#print(f"      fib_iter({num})={fib_iter(num)} in {timeit(lambda:fib_iter(num), number=1):.8f}s")

from math import sqrt

def fib_binet(n):
	## from https://artofproblemsolving.com/wiki/index.php/Binet%27s_Formula
	sqrt5 = sqrt(5)
	phi = (1 + sqrt5)/2
	psi = (1 - sqrt5)/2

	return int(((phi**n) - (psi**n))/sqrt5)

print(f"     fib_binet({num})={fib_binet(num)} in {timeit(lambda:fib_binet(num), number=1):.8f}s")
#print(f"     fib_binet({num})={fib_binet(num)} in {timeit(lambda:fib_binet(num), number=1):.8f}s")

def square(x):
	return x*x

def exp_fast(b, n):
	if n == 0:
		return 1
	elif n % 2 == 0:
		return square(exp_fast(b, n//2))
	else:
		return b * exp_fast(b, n-1)

def fib_binet_fast(n):
	## from https://artofproblemsolving.com/wiki/index.php/Binet%27s_Formula
	sqrt5 = sqrt(5)
	phi = (1 + sqrt5)/2
	psi = (1 - sqrt5)/2

	return int(((exp_fast(phi,n) - exp_fast(psi,n))/sqrt5))

print(f"fib_binet_fast({num})={fib_binet_fast(num)} in {timeit(lambda:fib_binet_fast(num), number=1):.8f}s")
#print(f"fib_binet_fast({num})={fib_binet_fast(num)} in {timeit(lambda:fib_binet_fast(num), number=1):.8f}s")

fibs = {}

def fib_memoize(n):
	if n < 2:
		return n
	else:
		if n in fibs:
			return fibs[n]
		else:
			fibn = fib_memoize(n - 1) + fib_memoize(n - 2)
			fibs[n] = fibn
			return fibn

print(f"   fib_memoize({num})={fib_memoize(num)} in {timeit(lambda:fib_memoize(num), number=1):.8f}s")
#print(f"   fib_memoize({num})={fib_memoize(num)} in {timeit(lambda:fib_memoize(num), number=1):.8f}s")