def myfunc(s):
    l = str()
    for i in range(0,len(s)):
        if i%2==0:
            l=l+s[i].lower()
        else:
            l = l+s[i].upper()
    return l
name = myfunc("Anthropomorphism")
print(name)
            
# Output: 'aNtHrOpOmOrPhIsM'
