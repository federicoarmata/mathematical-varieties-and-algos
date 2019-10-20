# mathematical_varieties_and_algos
interesting series, numbers and numerical challenges etc...

### Fibonacci Sequence

`python fibonacci.py`

Generate the first n numbers of the Fibonacci sequence using several algorithms and print the lower bound for the time of run for each of them.

The following convention has been used:

F(0) = 0
F(1) = 0, 1
F(2) = 0, 1, 1 

and so on.

### Pi

`python pi.py`

Generate pi (checked until the 1000-th decimal digit) with 2 different series:

1) using the Bailey–Borwein–Plouffe formula.
       
2) using a variation of the Bailey–Borwein–Plouffe formula found by F. Bellard.
   See http://mathworld.wolfram.com/PiFormulas.html for more details.
  
### Unique elements 

`python unique_elements.py`

Given a sorted array, write a function to extract the unique elements. 
Example: [1, 1, 3, 3, 3, 5, 5, 5, 9, 9, 9, 9], should return [1, 3, 5, 9].

### Horner's algorithm

`python Horners_algorithm.py`

Problem: Write an algorithm to compute: y = A_0+A_1*x+A_2*x^2+A_3*x^3+...+A_n*x^n.

Solution: A naive approach calculates each component of the polynomial and adds them up, this takes O(n^2) number of multiplication. We can use Horner algorithm to reduce the number of multiplications to O(n). The algorithm expresses the original polynomial differently and sequentially calculate: B_n=A_n, B_{n-1}=B_n*x+A_{n-1}, ..., B_0=B_1*x+A_0. We have y=B_0 with at most n multiplications.

### Moving average

`python moving_average.py`

Problem: Given a large array A of length m, build another array containing the n-element moving average of the moving average of the original array.

Solution: When we calculate the moving average of the next n consecutive numbers, we can reuse the previously computed moving averages. In pseuco-code:

S = A[1] + ... + A[n]; 
B[n] = S/n;
for (i from n+1 to m)
       S = S - A[i-n] + A[i]; 
       B[i] = S/n;

### Sorting

`python sorting_algorithms.py`

Problem: Write 3 sorting algorithms to sort n distinct values A_1, A_2, ..., A_n and analyse the complexity of each algo.

Solution:

1) Insertion sort
2) Merge sort
3) Quick sort






