#Ask user to enter age, gender ( M or F ) and then using following rules print their place of service.

#if employee is female, then she will work only in urban areas.

#if employee is a male and age is in between 20 to 40 then he may work in anywhere

#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

#And any other input of age should print "ERROR".

i=str(input("enter ur gender m or f:"))
a=int(input("enter ur age"))
if i=="f":
    print("she can work only in urban areas")
elif i=="m" and 20<a<40:  
    print("he can work anywhere")
elif i=="m" and 40<a<60:
    print("he can work only in urban area")
else:
    print("error")    
