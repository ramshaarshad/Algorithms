'''
Fibonacci without dynamic programming
'''
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
# print fib(40)

'''
Fibonacci Dynamic Programming
Memoization
'''
def fib_memo(n, memo):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if memo[n] == 0:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
print fib_memo(40, [0]*41)

'''
Fibonacci Dynamic Programming
Tabulation
'''
def fib_tab(n, tab):
    tab[0] = 0
    tab[1] = 1
    index = 2
    while index <= n:
        tab[index] = tab[index-1] + tab[index-2]
        index+=1
    return tab[n]
# print fib_tab(40, [0]*41)
