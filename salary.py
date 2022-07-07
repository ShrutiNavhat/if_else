# basic_salary=int(input("enter the number : "))
# HRA=basic_salary*(int(input("enter the number : "))/100)
# DA=basic_salary*(int(input("enter the number : "))/100)
# if basic_salary<=10000 and HRA==20 and DA==80:
#     print("low income")
# elif basic_salary<=20000 and HRA==25 and DA==90:
#     print("medium income")
# elif basic_salary>20000 and HRA==30 and DA==95:
#     print("high income")
# else:
#     print("below low income")

    

salary=int(input("enter the salary : "))
year=int(input("enter the year : "))
if year>=5:
    print("bonus")
    if salary//100*5:
        print(salary//100*5)
# elif year<5:
#         print("no bonus")
else:
    print("no bonus")
