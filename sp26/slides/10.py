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

#@trace1
def all_sevens(n):
	"Return True if the number is made up of all sevens"
	if n < 10:
		return n == 7
	else:
		return (n % 10 == 7) and all_sevens(n // 10)

#print(8,   all_sevens(8))
#print(7,   all_sevens(7))
#print(787, all_sevens(787))
#print(777, all_sevens(777))

def all_sevens_no_ifs(n):
	"Return True if the number is made up of all sevens"	
	return ((n < 10) and (n == 7)) or ((n % 10 == 7) and all_sevens_no_ifs(n // 10))

#print(8,   all_sevens_no_ifs(8))
#print(7,   all_sevens_no_ifs(7))
#print(787, all_sevens_no_ifs(787))
#print(777, all_sevens_no_ifs(777))

######################## TREE RECURSION ########################

@trace1
def fib(n):
	"Return the nth element of the Fibonacci sequence"
	if n < 2:
		return n
	else:
		return fib(n-1) + fib(n-2)

#print(fib(5))

######################## GAME THEORY SOLVER ########################

### Constants

WIN  = "win"
LOSE = "lose"

def generate_moves_10_to_0_by_1_or_2(position):
	return 0 if position == 0 else (1 if position == 1 else 12)

def generate_moves_25_to_0_by_1_3_or_4(position):
	return 0 if position == 0 else (1 if position < 3 else (13 if position == 3 else 134))

generate_moves = generate_moves_10_to_0_by_1_or_2
#generate_moves = generate_moves_25_to_0_by_1_3_or_4

def do_move(position, move):
	return position - move

def split_moves(moves):
	"Return all but last moves, and last move"
	return moves // 10, moves % 10

def graphviz_trace(solve):
	def solver_with_side_effects(position):
		moves = generate_moves(position)
		while moves:
			moves, move = split_moves(moves)
			print(position,"->",do_move(position,move))
		return solve(position)
	return solver_with_side_effects

#@graphviz_trace
def solve(position):
	"Return WIN|LOSE of the POSITION"
	moves = generate_moves(position)
	value = LOSE
	while moves:
		moves, move = split_moves(moves)
		child_position = do_move(position, move)
		child_value = solve(child_position)
		if child_value == LOSE:
			return WIN
	return value

def print_table(position):
	"Print a nice table of all the values from position to 0"
	while position > -1:
		print(position, solve(position))
		position -= 1

#print_table(10)

def print_digraph(position):
	"Print a digraph DOT format of the tree"
	print("digraph G {")
	while position > -1:
		moves = generate_moves(position)
		while moves:
			moves, move = split_moves(moves)
			print(position,"->",do_move(position,move))
		position -= 1
	print("}")

#print_digraph(10)

def print_all_solved_edges_digraph(position):
	"Print a digraph DOT format of all edges of the tree when solving"
	### solve needs to have the graphviz_trace decorator
	print("digraph G {")
	solve(position)
	print("}")

#print_all_solved_edges_digraph(10)