print("entry of new girl: ")
a=input("enter the girl name : ")
if a>="a" or a<="z":
    print("my name is",a)
    b=input("where are you from: ")
    if b=="1==Maharashtra" or "2==Out Of Maharashtra":
        print("ok so your from",b)
        A=input("your vacinated or not")
        if A=="1==I am not vacinated" or "2==I am vacinated":
            print("ok")
            if A==1:
                print("you will qurantine")
                if A==2:
                    print("you will not qurantine ")
                    
            c=input("ask qurantine incharge for room:  ")
            if c=="rani":
                print("room no 1")
            else:
                print("room not available")
        else:
            print("I am vaccinated")
    else:
        print("I am from out of maharashtra")
else:
    print("name")



                    
        
        