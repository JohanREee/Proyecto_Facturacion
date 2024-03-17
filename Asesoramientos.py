'''
def FullArnold():
    print("1. Full Arnold")
    print("💪 Este programa de entrenamiento completo, inspirado en la filosofía de Arnold Schwarzenegger, aborda todos los aspectos de la aptitud física y el desarrollo muscular. Con un enfoque integral en el entrenamiento de fuerza, resistencia, flexibilidad y nutrición, este programa está diseñado para aquellos que buscan alcanzar un nivel de acondicionamiento físico óptimo. A través de rutinas de entrenamiento avanzadas, técnicas de levantamiento de pesas probadas y asesoramiento nutricional personalizado, te ayudaré a esculpir tu cuerpo y a alcanzar tus objetivos de acondicionamiento físico con confianza y determinación.\n")

def FullBody():
    print("2. Full Body")
    print("🏋️‍♂️ El programa de entrenamiento Full Body está diseñado para proporcionarte un enfoque equilibrado en el fortalecimiento de todo tu cuerpo. Con sesiones de entrenamiento que abarcan todos los grupos musculares principales, este programa te ayudará a mejorar tu fuerza, resistencia y flexibilidad de manera integral. A través de una variedad de ejercicios funcionales y técnicas de entrenamiento efectivas, te guiaré para que logres un mayor rendimiento físico y una mejor salud general.\n")

def Tonificar():
    print("3. Tonificar")
    print("💪🏻 El programa de tonificación se centra en esculpir y definir tus músculos, proporcionando una apariencia más estilizada y tonificada. A través de ejercicios específicos de resistencia y trabajo con pesas moderadas, este programa te ayudará a desarrollar músculos magros y a reducir la grasa corporal. Con un enfoque en la mejora de la definición muscular y la creación de una apariencia más atlética, te guiaré para que logres resultados visibles y duraderos.\n")

def AsesoramientoBasico():
    print("4. Asesoramiento Básico")
    print("🤓 Este programa de asesoramiento básico es ideal para aquellos que están dando sus primeros pasos en el mundo del acondicionamiento físico y el ejercicio. A través de una combinación de asesoramiento personalizado y sesiones de entrenamiento simples, te proporcionaré los conocimientos y las herramientas básicas necesarias para comenzar tu viaje hacia un estilo de vida más saludable. Desde la introducción de ejercicios básicos de cuerpo completo hasta consejos sobre nutrición y hábitos saludables, este programa te ayudará a establecer una base sólida para tu bienestar físico y mental.\n")
'''

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