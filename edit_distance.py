'''
Given two strings str1 and str2, and below operations that can be performed on str1.
Find minimum number of edits required to convert str1 to str2.

a. Insert
b. Remove
c. Replace
'''

def edit_distance(str1, str2, l1, l2):
    '''
    l1 and l2 are lengths of str1 and str2 respectively
    '''
    if l1 == 0:  # If str1 is empty, you can only insert all characters from str2
        return l2
    if l2 == 0:  # If str2 if empty, you can only insert all characters from str1
        return l1

    if str1[l1-1] == str2[l2-1]:    # If the last two characters are the same, you can just move forward
        return edit_distance(str1, str2, l1-1, l2-1)

    return 1 + min(edit_distance(str1, str2, l1, l2-1),     # insert
                    edit_distance(str1, str2, l1-1, l2),    # remove
                    edit_distance(str1, str2, l1-1, l2-2)   # replace
                )
