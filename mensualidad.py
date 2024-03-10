import validaciones as v
import time_form as t
from cliente import ask
from archivo import createFileDir


def generarMembresia(type_of_payment):
    amount, name_payment = v.fileMonthlyPayment(type_of_payment)
    if amount is None:
        if not(ask('No se ha encontrado el archivo "mensualidad.json".\nDesea crearlo?')):
                return None
        createFileDir()
        list_payment = generarMembresia(type_of_payment)
        return list_payment
    current_time = t.getCurrentTime()
    day_amount = 0
    match name_payment:
        case 'month':
            day_amount = 30#check behaviour
        case 'fortknight':
            day_amount = 15
        case 'week':
            day_amount = 7
        case 'day':
            day_amount = 1
    notification_time= t.addTime(current_time, day_amount)
    return [amount, name_payment, notification_time]
            

            
        





