def compound_interest(p,t,r):
    #ci = p*(pow((1+r/100),t))
    ci = p*((1+r/100)**t)
    return ci
    
p,t,r = 1200, 2, 5.4
s = compound_interest(p,t,r)
print("The Principle is ",p)
print("The time is ",t)
print("The rate of interest is ",r)
print("the simple interest is ",s)
