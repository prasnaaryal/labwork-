#A student will not be allowed to sit in exam if his/her attendence is less than 75%.

#Take following input from user

#Number of classes held

#Number of classes attended.

#And print

#percentage of class attended

#Is student is allowed to sit in exam or not.

num_classheld=int(input("enter the number of classes held"))
num_classjoined=int(input("enter the number of classes attended"))
percentage_classheld=num_classjoined%num_classheld*100
print("the percentage of classes attended is",percentage_classheld)
if percentage_classheld>=75:
    print("student is allowed to sit in exam")
else:
    print("student isn't allowed to sit in exams")
