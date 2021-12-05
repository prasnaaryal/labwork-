distance=4
time_spent_on_stopping=2*10
bus_journey=25%distance
total_time=(time_spent_on_stopping+bus_journey)
print (total_time)
j1=(1//7)
j2=(2//15)
j3=(1//7)
journey_jogging=j1+j2+j3
if journey_jogging>total_time:
      print(f'jogging is faster')
else:
    print(f'bus is faster')
