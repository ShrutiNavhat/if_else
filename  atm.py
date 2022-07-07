print("Welcome")
print("Isert your card")
card=input("enter the card : ")
if card=="credit card" or card=="debit card":
    print("next")
    l=input("enter the language :")
    if l=="english":
        print("next")
        p=input("enter the your pin :")
        if len(p)==4:
            print(p,"your pin code is right")
            b=input("enter the your bank : ")
            if b=="SBI" or b=="" or b=="":
                print(b)
                a=int(input("what you want withdrawal/check your bank balance :"))
                if a==10000:
                    print(a)
                    w=int(input("enter your withdrawal amount :"))
                    if a-w:
                        print("your balance is=",a-w)
                        r=input("you want reciept yes or no : ")
                        if r=="yes" or r=="no":
                            print("ok")
                            print("done")
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
    elif l=="hindi":
        print("ok") 
        P=input("pin daliye : ")   
        if len(P)==4:
            print(P,"tumhara pin code sahi hai") 
            B=input("bank ka nam daliye : ")
            if B=="SBI" or B=="" or B==""  :
                print(B) 
                A=int(input("tumhe kitne  paise nikalne hai ya kitne baki hai dekhna hai :"))
                if A==10000:
                    print(A)
                    W=int(input("kitne paise chahiye  daliye:"))
                    if A-W:
                        print("tumhare pass ",A-W,"paise baki hai")
                        R=input("tumhe perchi chahiye ya nhi : ")
                        if R=="ha" or R=="nhi":
                            print("ok")
                            print("done")
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
    print("wtong")