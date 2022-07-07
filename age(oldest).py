

a=int(input("enter the number : "))
b=int(input("enter the number : "))
c=int(input("enter the number : "))
d=int(input("enter the number : "))
if a>b and a>c and a>d:
    print("a is oldest")
elif b>a and b>c and b>d:
    print("b is oldest")
elif c>a and c>b and c>d:
    print("c is oldest")
else:
    print("oldest")
