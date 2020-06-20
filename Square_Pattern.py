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
