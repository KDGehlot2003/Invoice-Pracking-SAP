from datetime import datetime


x_date = datetime.now()

# print(x_date)
# print(type(x_date))
# date = x_date.strftime("%d-%B-%Y")


date = "23-May-23"
xdate = "18-May-23"


date_object = datetime.strptime(date, '%d-%b-%y').date()
dt = datetime.strptime(xdate, '%d-%b-%y').date()

dates = [date_object,dt]


# print(dt)
# print(date_object)
# print(type(date_object))

# print(max(dates))
x  =  max(dates)


print("dd.mm.yy:", x.strftime("%d.%m.%y"))


