'''
Given a string, find longest substring without repeating characters
'''
def longestSubString(s):
    words = {}
    longest = ''
    current = ''

    for i in range(len(s)):
        if s[i] in words :   # if the character already appeared
            words = {} #reset words
            words[s[i]] = 1 #take the current char into account
            if len(current) >= len(longest): # if the substring is longer than the previous substring
                longest = current
            current = s[i] # reset current substring
        else:                   # if the character hasnt appeared yet
            words[s[i]] = 1     # track that the character has appeared
            current += s[i]
    return longest
