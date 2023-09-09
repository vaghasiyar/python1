ss=int(input("enter a value "))
gk=int(input("enter a value "))
sci=int(input("enter a value "))
total=ss+gk+sci
print(total)
per=(total*100)/300
print(per)
if (per>75):
    print("grade A")
elif(per>60 and per<75):
    print("grade B")
elif(per>45 and per<60):
    print("grade C")
elif(per>35 and per<45):
    print("grade D")
else:
    print("fail")
