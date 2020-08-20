import re
s = input("Enter identifier:")
m = re.fullmatch("[a-k][0369][a-zA-Z0-9#]*",s)
if m!=None:
    print(s," is valid Yava identifier")
else:
    print(s," is invalid Yava identifier")
    
    
Output:

Enter Identifier:a6kk9z##
a6kk9z## is valid Yava Identifier

Enter Identifier:k9b876
k9b876 is valid Yava Identifier

Enter Identifier:k7b9
k7b9 is invalid Yava Identifier
