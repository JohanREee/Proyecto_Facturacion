from time import *

def getCurrentTime():
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
        
def validateTime(expiration_time): #True, False
    current_time =  getCurrentTime()
    current_year, current_month, current_day = current_time
    expiration_year, expiration_month, expiration_day = expiration_time

    if(current_year == expiration_year and current_month == expiration_month and current_day > expiration_day): #2024, 2025
        return False
    elif(current_year == expiration_month and current_month > expiration_month):
        return False
    elif(current_year > expiration_year):
        return False
    return True

def showDate(time):
    return f"{time[2]}/{time[1]}/{time[0]}"

if __name__ == "__main__":
    pass