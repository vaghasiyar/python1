n=int(input("enter a value"))
for i in range(n):
    for j in range(n-i):
            print(" ",end="")
    for j in range(n):
            print("*",end="")
    print()
