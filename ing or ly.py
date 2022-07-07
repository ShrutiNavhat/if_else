# a=input("enter the word :")
# if a>="a" and a<="z":
#     print(a)
# if a+"ing"==1:
#     print(a+"ing"!=2)
# if a+"ing":
#     print(a+"ing")
# elif a+"ing" and a+"ly":
#     print(a+"ly")



n=input("Enter your character:")
a="ing"
b="ly"
if "ing" in n:
    print(n+b)
elif n>="a" and n<="z":
    print(n+a)
else:
    print("no")