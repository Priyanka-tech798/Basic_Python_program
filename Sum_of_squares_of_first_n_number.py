"""
I/p : N = 4
O/p : 30
1**2 + 2**2 + 3**2 + 4**2
= 1 + 4 + 9 + 16
= 30
"""

def squaresum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum+(i**2)
    print("The Result is ",sum)    

n = int(input("Enter a number:"))
squaresum(n)
