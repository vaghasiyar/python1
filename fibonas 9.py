a,b=0,1
n=int(input("enter a number"))
for i in range (1,n+1):
    c=a+b
    print(c) 
    a=b
    b=c
