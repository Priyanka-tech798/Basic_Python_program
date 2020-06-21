s=input("Enter a string to search for vowels: ")
v=['a','e','i','o','u','A','I','E','O','U']
d={}
for ch in s:
    if ch in v:
        d[ch]=d.get(ch,0)+1
for k,v in sorted(d.items()):
    print("{} occurs {} times".format(k,v))
		
		
		
		
		
Enter a string to search for vowels: Django is a framework

a occurs 3 times
e occurs 1 times
i occurs 1 times
o occurs 2 times
