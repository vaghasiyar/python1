n = int(input("enter a value")) 
for i in range(n):
    for j in range(i):
        print("   ", end="")
    for j in range(n - i):
        if j == 0 or j == n - i - 1 or i == 0 or i == n - 1:
            print("*  ", end="")
        else:
            print("   ", end="")
    print()
