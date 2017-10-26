'''
Fibonacci Dynamic Programming
'''
def fib(n, memo):
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
print fib(7, [0]*100)
