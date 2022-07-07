a=int(input("enter the number :"))
if a%35==0:
    print("it is divisible by 35")
    if a%7==0 and a%5==0:
        print("it is divisible by 7 abd 5")
else:
    print("it is not divisible ")