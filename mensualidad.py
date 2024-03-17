import validaciones as v
import time_form as t

from archivo import createFilesDirectory


def generarMembresia(type_of_payment,mensualidad_dias):
    amount, name_payment = v.fileMonthlyPayment(type_of_payment)
    if amount is None:
        createFilesDirectory()
        list_payment, days = generarMembresia(type_of_payment,mensualidad_dias)
        return list_payment, days
    current_time = t.getCurrentTime()
    day_amount = 0
    formal_name_payment = None
    match name_payment:
        case 'month':
            day_amount = 30
            formal_name_payment = 'Mensual' 
        case 'fortknight':
            day_amount = 15
            formal_name_payment = 'Quincenal'
        case 'week':
            day_amount = 7
            formal_name_payment = 'Semanal'
        case 'day':
            day_amount = 1
            formal_name_payment = 'Diario'
    day_amount += mensualidad_dias
    notification_time= t.addTime(current_time, day_amount)
    return [formal_name_payment,amount, notification_time], mensualidad_dias + day_amount

if __name__ == "__main__":
    pass
            
        





