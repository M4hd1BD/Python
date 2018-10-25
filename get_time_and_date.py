from datetime import datetime,timedelta,timezone,date

today = date.today()

dat = today.strftime('%a, %-d %b, %y')

z = input("Enter your timezone:")

now = datetime.utcnow() + timedelta(hours = int(z))

time = now.strftime('%I:%M %p')

day = "Today is %s" %(dat)

print(day)

tm = 'Time is %s' %(time)

print(tm)
