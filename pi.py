from mpmath import *

def pi_generator1(N):
    """
    Calculates pi using Bailey–Borwein–Plouffe formula.
    Checked until 1000-th decimal digit.
    """
    
    pi = mpf(0)
    #setting precision
    mp.dps = N + 1 
    
    for i in range(0, N):
        #n:numerator
        # d:denominator of the series
        n = (
            mpf(4)/mpf(8*i+1)
            -mpf(2)/mpf(8*i+4)
            -mpf(1)/mpf(8*i+5)
            -mpf(1)/mpf(8*i+6))
        d = mpf(16)**i
        pi += n/d
    return pi


def pi_generator2(N):
    """
    Calculates pi using a variation of the Bailey–Borwein–Plouffe
    formula found by F. Bellard.
    See http://mathworld.wolfram.com/PiFormulas.html for more details.
    Checked until 1000-th decimal digit
    """
    
    pi = mpf(0)
    mp.dps = N + 1
    x=0
    
    if N > 1000:
        x == N
    
    for i in range(0,x+350):
        n1 = mpf((-1)**i)
        n2 = (
            -mpf(2**5)/mpf(4*i+1)
            -mpf(1)/mpf(4*i+3)
            +mpf(2**8)/mpf(10*i+1)
            -mpf(2**6)/mpf(10*i+3)
            -mpf(2**2)/mpf(10*i+5)
            -mpf(2**2)/mpf(10*i+7)
            +mpf(1)/mpf(10*i+9))
        d = mpf(2**(10*i))
        pi += n1*n2/d
    return pi/mpf(2**6)


def print_pi(N, generator):
    """
    Print pi to the N-th decimal digit (rounding)
    """
    print(nstr(generator(N), N+1))


if __name__ == "__main__":

    N = 100
    
    print_pi(N, pi_generator1)
    print_pi(N, pi_generator2)



