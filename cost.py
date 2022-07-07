cost=int(input("enter the amount : "))
if cost<1000:
    print("no discount")
elif cost>=1000:
    print(cost//10,"10%  discount")
else:
    print("more discount")