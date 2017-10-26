'''
Return all of the palindromes in a given string
'''
def palindrome(s):
    if len(s) == 1 or len(s) == 0:
        return []
    if palindrome_helper(s):
        return [s] + palindrome(s[:-1]) + palindrome(s[1:])
    return palindrome(s[:-1]) + palindrome(s[1:])

def palindrome_fast(s, memo):
    if len(s) == 1 or len(s) == 0:
        return []
    try:    # s was cached
        if memo[s]:
            return []
    except: # s was not cached
        if palindrome_helper(s):
            memo[s] = 1
            return [s] + palindrome_fast(s[:-1], memo) + palindrome_fast(s[1:], memo)
        return palindrome_fast(s[:-1], memo) + palindrome_fast(s[1:], memo)


def palindrome_helper(s):   # check if s is a palindrome
    if len(s) == 1 or len(s) == 0:
        return 1
    if s[0] != s[-1]:
        return 0
    return palindrome_helper(s[1:-1])

print palindrome_fast('abaab', {})
