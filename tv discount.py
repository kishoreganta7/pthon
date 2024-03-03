
tv1,tv2=map(int,input().split())
x,y=map(int,input().split())
tv1-=(tv1*x)//100
tv2-=(tv2*x)//100
if tv1<tv2:
    print("buy tv1")
elif tv1>tv2:
    print("buy tv2")
else:
    print("any")

