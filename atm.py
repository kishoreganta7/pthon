a=int(input("enter account balance:"))
b=int(input("withdraw amount:"))
if b<=a:
    if b%5==0:
        a-=b
        print(a-0.50)
    else:
        print("notmultipule of 5")
    
else:
    print( a )


    

