
#####################################################
## Problem:
## Swap 2 integers, without using additional storage
## space.
######################################################

def swap_two_numbers(x, y):
    
    #this requires the use of z (other temporary variable)
    z = y
    y = x
    x = z

    return x, y

swap_two_numbers(2, 3)

def swap_two_numbers_without_temporary_storage(x, y):

    x = x + y # store the sum of x and y
    y = x - y #change y to x's value
    x = x - y #change x to y's value

    return x, y

swap_two_numbers_without_temporary_storage(2, 3)




