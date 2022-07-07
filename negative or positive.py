num=int(input("enter num:"))
if num>0:
        print("positive")
        if num%2==0:
            print("even")
        else:
            print("odd")
elif num<0:
        print("negative")
        if num%2==0:
            print("even")
        else:
            print("odd")
else:
        print("zero")

