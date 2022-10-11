a=int(input("enter the number"))
if a%7==0:
    if a%5==0:
        if a>1500 and a<2700:
            print("it is divisible by 7 & 5 and it is 1500 and 2700")
        else:
            print("it is not 1500 and 2700")
    else:
        print("it is not divisible by 5")
else:
    print("it is not divisible by 7")
    