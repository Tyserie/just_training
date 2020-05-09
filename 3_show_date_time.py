import datetime

x = datetime.datetime.now()
print("The date now is", x.strftime("%d-%m-%Y"), "and the time is", x.strftime("%H:%M:%S"))

#Capital Y shows whole year, small y shows last two NRs of year
#I can swap the positions of %d %m etc.
