from validaciones import decoratorvalidate
from time_form import getCurrentTime, addTime

@decoratorvalidate
def getPriceConsultancy():
    price = float(input('Digite el precio a pagar para este asesoramiento: $'))
    if not(25<=price<=100):
        raise ValueError
    return price

def generarAsesoramiento(type_of_consultancy, asesoramiento_dias):
    asesoramiento_dias +=30
    price = getPriceConsultancy()
    time = getCurrentTime()
    expiration_time = addTime(time, asesoramiento_dias)
    return [type_of_consultancy, price, expiration_time], asesoramiento_dias
        
if __name__ == "__main__":
    pass