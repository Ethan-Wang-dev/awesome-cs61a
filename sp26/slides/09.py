def trace1(f):
	### from https://cs61a.rouxl.es/docs/week-3/content/decorators/
    def traced(x):
        print(f"Input : {x}")
        result = f(x)
        print(f"Output: {result}")
        return result
    return traced

def trace2(f):
	### from https://cs61a.rouxl.es/docs/week-3/content/decorators/
    def traced(x,y):
        print(f"Input : {x},{y}")
        result = f(x,y)
        print(f"Output: {result}")
        return result
    return traced

def downup_iter(n):
	"print the numbers from n down to 0 and up to n"
	n_original = n
	while(n):
		print(n)
		n = n - 1
	while(n <= n_original):
		print(n)
		n = n + 1

#downup_iter(3)

def downup_recursive(n):
	"print the numbers from n down to 0 and up to n"
	if n == 0:
		print(n)
	else:
		print(n)
		downup_recursive(n-1)
		print(n)

#downup_recursive(3)

### digits

def digits_iter(n):
	"Return the number of digits in positive integer n"
	count = 0
	while n:
		n, count = n // 10, count + 1
	return count

#print(digits_iter(9))
#print(digits_iter(123))

@trace1
def digits_recursive(n):
	"Return the number of digits in positive integer n"
	if n == 0:
		return 0
	else:
		return 1 + digits_recursive(n // 10)

#print(digits_recursive(9))
#print(digits_recursive(123))

def digits_tail_recursive(n):
	"Return the number of digits in positive integer n"
	return digits_tail_recursive_helper(n, 0)

@trace2
def digits_tail_recursive_helper(n, sum):
	if n == 0:
		return sum
	else:
		return digits_tail_recursive_helper(n // 10, sum + 1)

#print(digits_tail_recursive(9))
#print(digits_tail_recursive(123))
