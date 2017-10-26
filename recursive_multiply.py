def recursive_mult(x,y):
    if x==0 or y == 0:
        return 0
    return x + recursive_mult(x, y-1)

print recursive_mult(4,6)
print '24'
