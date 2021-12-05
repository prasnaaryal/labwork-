#wap to print the time after taking the amount of seconds passed from midnight as input from the user
time=int(input("enter the time passed in sec"))
hours=time//60
min=time%60
print(hours,min)