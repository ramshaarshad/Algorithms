'''
You are given a list of ints and a target int.
you must return pairs of ints in the list that sum to the target.
Each element in the list must be used only once.
'''

# slow O(n^2)
def sum_to_target(n, t):
    if len(n) == 0 or len(n) == 1:
        return []
    first = n[0]
    part = n[1:]
    for x in range(len(part)):
        if first+part[x] == t:
            return [[first,part[x]]] + sum_to_target(part[:x]+part[x+1:],t)
    return sum_to_target(part, t)
# print sum_to_target([4,8,5,7,6,1,5,2,6],12)

# fast O(n)
def sum_to_target_fast(n, t):
    returnList = []
    memo = [0]*50   # ask what will be the biggest number
    for x in n:
        diff = abs(t-x)
        if memo[diff]:
            returnList += [[x,diff]]
        else:
            memo[x] = 1
    return returnList
print sum_to_target_fast([4,8,5,7,6,1,5,2,6],12)
