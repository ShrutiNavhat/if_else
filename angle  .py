a=int(input("enter the angle : "))
b=int(input("enter the angle : "))
c=int(input("enter the angle : "))
if a+b+c==180:
    print("given angle is valid")
else:
    print("given angle is not valid")

a=int(input("enter the side : "))
b=int(input("enter the side : "))
c=int(input("enter the side : "))
if a==b==c:
    print("equilateral triangle")
elif a!=b!=c:
    print("scalene triangle")
else:
    print("isosceles triangle")


# a=int(input("enter the number : "))
# b=int(input("enter the number : "))
# c=int(input("enter the number : "))
# if a<b<c and b<c<a and c<a<b:
#     print("youngest")
# if a>b>c and b>c>a and c>a>b:
#     print("oldest")
# else:
#     print("equal")