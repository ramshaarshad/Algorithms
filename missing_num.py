'''
pg 189
n is an unsorted array containing the numbers from 1 to N except 1

find the missing number

Fast solution should do it in O(n) time and O(1) space
'''

# do the sum of all the numbers there and subtract that from the sum of all the numbers that should be there
# not 100% sure if this works but it should, comcept is definitely accurate
def missing_num(n):
    x = sum(n)
    y = sum(range(len(n)))
    return y-x
