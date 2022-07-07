cost_price=int(input("enter the price : "))
tex=int(input("enter the tex : "))
if cost_price>100000:
    print("paid rode tex")
    if cost_price//100*15:
        print(cost_price//100*15,"is tex amount")
elif cost_price>50000 and cost_price<=100000:
    print("paid rode tex")
    if cost_price/100*10:
        print(cost_price//100*10,"is tex amount")
elif cost_price>50000:
    print("paid rode  tex")
    if cost_price//100*5:
        print(cost_price/100*5,"is tex amount")
    # else:
    #     print("no tex")
else:
    print("no tex")


# cost_price=int(input("enter the price : "))
# # tex=int(input("enter the tex : "))
# if cost_price>100000:
#     a=cost_price%15
#     print()
