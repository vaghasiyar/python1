sum=0
n=int(input("enter a number"))
digit_str=str(n)
for i in digit_str:
    int_i=int(i)
    sum+=int_i
print(sum)
