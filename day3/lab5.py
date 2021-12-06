#4. Given three integers, print the smallest one. (Three integers should be user input) 
a=int(input("enter a integer"))
b=int(input("enter a integer"))
c=int(input("enter a integer"))
if a<b or a<c:
    print("a is the smallest")
elif b<a or b<c:
    print("b is the smallest")
else:
    print("c is the smallest")