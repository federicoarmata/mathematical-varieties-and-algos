##############################################################
## Problem:
## Given a large array A of length m, build another array 
## containing the n-element moving average of the moving 
## average of the original array:
## B1, ..., B_{n-1}=N*A, B_i=(A_{i-n+1}+A_{i-n+2}+...+A_i)/n, 
## for each i=n,...,m.
###############################################################

def calculate_moving_average(A, n):
    """
    Parameters:
    ----------
    A:
        list object, on which we calculate the moving average
    n:
        element to consider for the moving average

    Output:
    ------
    B:
        list object, containing the moving average.
    
    """

    if n<=0 or type(n)!= int:
        print("n must be a positive integer ")
        B=None
    else:
        B = []
        B.append(sum(A[:n])/n)
        b0 = B[0]
        for i in range(n, len(A)):
            print(i)
            S = (b0*n-A[i-n]+A[i])/n
            B.append(S)
            b0 = S

    return B

calculate_moving_average([1, 2, 3, 4, 5], 0)