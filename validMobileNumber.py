import re
n = input("Enter mobile number:")
m = re.fullmatch("[7-9]\d{9}",n)
if m!=None:
    print("Valid mobile number")
else:
    print("invalid mobile number")

Output: 

Enter mobile number:9898989898
Valid Mobile Number

Enter mobile number:6786786787
Invalid Mobile Number
