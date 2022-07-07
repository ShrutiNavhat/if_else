# num=int(input("enter the number : "))
# a=num%10
# b=(num//10)%10
# c=(num//100)%10
# d=(num//1000)%10
# if num>=1:
#     print(a,b,c,d)
# else:
#     print("no")


# a=int(input("enter the age : "))
# b=int(input("enter the age : "))
# c=int(input("enter the age : "))
# if a<b and a<c:
#     print(a,"youngest")
# if a>b and a>c:
#     print(a,"oldest")
# if b<a and b<c:
#     print(b"youngest")
# if b>a and b>c:
#     print(b"oldest")
# if c<a and c<b:
#     print(c,"youngest")
# if c>a and c>b:
#     print(c,"oldest")
# else:
#     print("equal")


# # a=int(input("enter the number : "))
# # if a*a:
# #     print(a*a,"squer")
# # else:
# #     print("not squer")
i=int(input("enter the number : "))
rev=0
rev=(rev*10)+i%10
i=i//10
print(rev)