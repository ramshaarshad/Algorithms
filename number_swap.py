'''
Swap the value of two int variables without using a third variable
'''
def number_swap(x,y):
    print x,y
    x = x+y
    y = x-y
    x = x-y
    print x,y
number_swap(5.1,6.3)

def number_swap_bit(x,y):
    print x,y
    x = x^y
    y = x^y
    x = x^y
    print x,y
print '\n'
number_swap_bit(5,6)
