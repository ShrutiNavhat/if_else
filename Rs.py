day=int(input("enter the day :"))
if day<=5:
    print("2Rs")
elif day>=6 or day<=10:
    print("3Rs")
elif day>=10 or day<=15:
    print("4Rs")
else:
    print("5Rs")