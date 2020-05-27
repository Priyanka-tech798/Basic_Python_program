"""
Simple interest formula is given by:
Simple Interest = (P x T x R)/100
Where,
P is the principle amount
T is the time and
R is the rate
"""


def simple_interest(p,t,r):   
    si= (p*t*r)/100
    return si
    
p,t,r = 1000, 7, 1.5
s = simple_interest(p,t,r)
print("The Principle is ",p)
print("The time is ",t)
print("The rate of interest is ",r)
print("the simple interest is ",s)
