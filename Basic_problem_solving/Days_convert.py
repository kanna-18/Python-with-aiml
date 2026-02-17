n=int(input("enter no of days"))
y=n//365
n=n-y*365
m=n//30
n=n-m*30
w=n//7
n=n-m*7
d=n
print(y,"year",m,"month",w,"weak",d,"days")
