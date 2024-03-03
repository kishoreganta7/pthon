x,y=map(int,input().split())
if x<=y:
    np=0
else:
    c=x-y
    if c%4==0:
        np=c//4
    else:
        np=(c//4)+1
print(np)
