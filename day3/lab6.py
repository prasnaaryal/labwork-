#2. WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 
a=int(input("enter the marks of first subject "))
b=int(input("enter the marks of second subject "))
c=int(input("enter the marks of third subject "))
d=int(input("enter the marks of fourth subject "))
total_marks=a+b+c+d
print(f"total is{total_marks}")
pera=(total_marks)/400*100
print(f"pera is final percentage{pera}")
if pera>70:
    print("distinction")
elif pera>60:
    print("first")
elif pera>40:
    print("pass")
elif pera<40:
    print("fail")
else:
    print("please input valid marks")
