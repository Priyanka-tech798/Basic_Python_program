#To generate Fibonacci Numbers...
#The next is the sum of previous 2 numbers
#Eg: 0,1,1,2,3,5,8,13,21,...


def fib():
    a,b =0,1
    while True:
        yield a
        a,b = b,a+b
for f in fib():
    if f>100:
        break
    print(f)
