x=input("enter own character")
if (x>="a" and x<="z") or (x>="A" and x<="Z"):
    print(x,"is an alphabet")
elif (x>="0" and x<="9"):
    print(x,"is an digit")
else:
    print(x,"is an special character")
    