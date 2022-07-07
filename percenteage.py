maths=int(input("enter the marks : "))
chem=int(input("enter the marks : "))
bio=int(input("enter the marks : "))
phy=int(input("enter the marks : "))
com=int(input("enter the marks : "))
a=(maths+chem+bio+phy+com)/500*100
if a>=90:
    print("A grade",a)
elif a>=80:
    print("B grade",a)
elif a>=70:
    print("C grade",a)
elif a>=60:
    print("D grade",a)
else:
    print("f grade")