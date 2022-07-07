x=input("enter the phone no.")
if len(x)==10:
    print("your phone no =",x)
    a=input("enter the email : ")
    if a+"@gmail.com":
        print(a+"@gmail.com")
        y=input("enter the password : ")
        if len(y)>=8:
            print(y)
            b=input("enter the first name : ")
            if b>="a" and b<="z":
                print(b)
                c=input("enter the surname : ")
                if c>="a" or c<="z":
                    print(c)
                    d=input("enter the birth date : ")
                    if d>="1" and d<="9":
                        print(d)
                        e=input("enter the gender :  ")
                        if e=="female" or e=="male" or e=="other":
                            print(e)
                            print("you have successfully created your account")
                        else:
                            print("wrong")
                    else:
                        print("wrong")
                else:
                    print("wrong")        
            else:
                print("wrong")
        else:
            print("wrong")
    else:
        print("wrong") 
else:
    print("wrong")       