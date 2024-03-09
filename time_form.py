from time import *

def getActualTime():
    actual = localtime()
    return [actual[0], actual[1], actual[2]]

def leapYear(year):
    return (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0)

def addTime(time, dias_cantidad = 7): 

    year, month, day = time[0],time[1],time[2]
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if(month == 2 and leapYear(year)):
        month_days[1] = 29

    day += dias_cantidad
    while day > month_days[month-1]:
        day -= month_days[month-1]
        month +=1
        if month > 12:
            month = 1
            year +=1
    return [year, month, day]
        
time = getActualTime()
list_time= addTime(time, 10)