n = int(input("enter a value"))
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()
for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        print("*", end=" ")
    print()
