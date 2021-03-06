#fibonacci
def fib(x): 
	if x <= 2:
		return 1
	return fib(x-1)+fib(x-2)

# or with lambda 
fib = lambda x: 1 if x <= 2 else fib(x-1) + fib(x-2)
