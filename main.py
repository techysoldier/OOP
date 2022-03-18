from time import time
from alarmclock import Alarm, current, switch


my_alarm = Alarm('11:00')
print(Alarm, my_alarm.wake)



my_alarm = switch
print(input('Y or N')) 
print('Alarm is set for', my_alarm)

my_time = current("9:00")
print('9am')



 