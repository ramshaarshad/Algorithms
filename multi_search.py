'''
pg 149
s is a string
t is an array of strings that are shorter than s

return all of the strings in t that are sub strings of s

ex: s = 'string' t = ['tring', 'str', 'ing', 'bu', 'bc']
    returns: ['tring', 'str', 'ing']
'''

# inefficient solution O(n^4)
def multi_search(s, t):
    if t[0] in s:
        return [t[0]] + multi_search(s, t[1:])
    return []
print multi_search('string', ['tring', 'str', 'ing', 'bu', 'bc'])

# efficient solution

### IN PROGRESS ###
# def multi_search_fast(s, t):
