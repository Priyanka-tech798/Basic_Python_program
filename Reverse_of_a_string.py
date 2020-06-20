s = input("Enter a string to reverse: ")
rv = s[::-1]
print(rv)

r=reversed(s)
op="".join(r)
print(op)

reverse_string=""
i= len(s)-1
while i>=0:
    reverse_string+=s[i]
    i-=1
print(reverse_string)



Enter a string to reverse: Django
ognajD
