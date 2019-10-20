###############################################################
## Problem:
## Algo to compute:
## y = A_0+A_1*x+A_2*x^2+A_3*x^3+...+A_n*x^n,
## A naive approach calculates each component of the polynomial
## and adds them up, this takes O(n^2) number of multiplication,
## while Horner algo takes O(n).
################################################################

def calculate_polynomial(A, x):
    """
    Algo:
    B_n=A_n, B_{n-1}=B_n*x+A_{n-1}, ..., B_0=B_1*x+A_0

    Parameters:
    ----------
    A:
        list object of the coefficients A_n, 
        sorted from 0 order;
    x:
        scalar number, value on which we calculate the
        polynomial.

    Output:
    -------
    y: 
        float number, sum of the terms in the 
        polynomial.
    """

    Bn = A[-1]
    for n in range(len(A)-1, 1, -1):
        print(n)
        Bn_minus_1 = Bn*x+A[n-1]
        Bn = Bn_minus_1
        
    y = Bn_minus_1*x+A[0]
    
    return y


calculate_polynomial([1, 2, 3, 4, 5], 1)