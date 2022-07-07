a=int(input("enter the age : "))
b=int(input("enter the age : "))
c=int(input("enter the age : "))
d=int(input("enter the age : "))
if  a<b and a<c and a<d:
    print("a is youngest")
elif b<a and b<c and b<d:
    print("b is youngest")
elif c<a and c<b and c<d:
    print("c is youngest")
else:
    print("d is youngest")