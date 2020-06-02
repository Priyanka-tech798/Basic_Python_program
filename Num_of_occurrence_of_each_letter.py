word = input("Enter a word: ")
d={}
for x in word:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    print(k,"occurred",v,"times")
    
    
    Output:-
-------------------------    
Enter a word: mississippi
m occurred 1 times
i occurred 4 times
s occurred 4 times
p occurred 2 times
