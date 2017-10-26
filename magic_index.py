'''
Return the magic index in the array if it exists. The elements in the array are ordered

Magic index is when A[i] = i
'''
n = [-40,-20,-1,1,2,3,5,7,9,12,13]

# Brute forse O(n)
def magic_index(n):
    for i in range(len(n)):
        if n[i] == i:
            return i
    return None

def magic_index_dynamic(n):
    return magic_index_dynamic_help(n, 0, len(n)-1)

def magic_index_dynamic_help(n, start, end):
    if start > end:
        return None
    mid = (start+end) / 2
    if n[mid] == mid:
        return mid
    if n[mid] > mid:
        return magic_index_dynamic_help(n, start, mid-1)
    return magic_index_dynamic_help(n, mid+1, end)


'''
Input array now contains non distinct integers
'''
n2= [-10,-5,2,2,2,3,4,7,9,12,13]
def magic_index_dynamic_nd(n):
    return magic_index_dynamic_nd_help(na, 0, len(n2)-1)

def magic_index_dynamic_nd_help(n, start, end):
    if start > end:
        return None
    mid = (start + end) / 2
    if n[mid] == mid:
        return mid
    # search left
    leftEndIndex = min(mid-1, n[mid])
    left = magic_index_dynamic_nd_help(n, start, leftEndIndex)
    if left:
        return left
    # search right
    rightStartIndex = max(mid+1, n[mid])
    right = magic_index_dynamic_nd_help(n, rightStartIndex, end)
    return right
print magic_index_dynamic_nd(n2)
