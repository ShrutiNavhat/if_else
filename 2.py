alp=input("enter the alphabet: ")
special_character=input("enter the special_character: ")
num=input("enter the number: ")
if alp>="a" and alp<="z" or alp>="A" and alp<="Z":
    print("alphabet")
if special_character=="@" or special_character=="#" or special_character=="$":
    print("special_character")
if num:
    print(num) 
if alp>="a" and alp<="z" and special_character and num:
    print(alp+special_character+str(num))
else:
    print("not strong password")



# x=int(input("enter the number : "))
# if (x%10)%5==0:
#     print("divisible")
# else:
#     print("not divisible")


if False:
    print("no")
    if True:
        print("yes")
    elif True:
        print("yes")
    else:
        print("no")
elif True:
    print("yes")
    if True:
        print("yes")
    elif True:
        print("yes")
    else:
        print("no")
else:
    print("no")


    # n=int(input("Enter your number:"))
# if n%2==0:
#     print(-n)
# else:
#     print(n)
    