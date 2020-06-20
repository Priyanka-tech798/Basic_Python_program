n=int(input("Enter a value: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
    
    
Enter a value: 5
*
* *
* * *
* * * *
* * * * *
    
n=int(input("Enter a value: "))
for i in range(n):
    print("*"*(n-i))
    
Enter a value: 5
*****
****
***
**
*

n=int(input("Enter a value: "))
for i in range(n):
    print((' '*(n-i-1)) +("* ")*(i+1))
    
Enter a value: 7
      *
     * *
    * * *
   * * * *
  * * * * *
 * * * * * *
* * * * * * *

n=int(input("Enter a value: "))
for i in range(n):
    print(" "*i+'* '*(n-i))
    
 Enter a value: 7
* * * * * * *
 * * * * * *
  * * * * *
   * * * *
    * * *
     * *
      *   
