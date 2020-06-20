n=int(input("Enter a value: "))
for i in range(n):
    print("*",end=" ")

Enter a value: 5
* * * * *



n=int(input("Enter a value: ")) 
for i in range(n):
    print("*"*n)

Enter a value: 5
*****
*****
*****
*****
*****


n=int(input("Enter a value: "))
for i in range(n):
    print((str(i+1)+" ")*n)

Enter a value: 8
1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8


n=int(input("Enter a value: "))
for i in range(n):
    print((chr(65+i)+" ")*n)
    
Enter a value: 6
A A A A A A
B B B B B B
C C C C C C
D D D D D D
E E E E E E
F F F F F F
