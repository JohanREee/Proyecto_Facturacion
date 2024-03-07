from validaciones import *

def proteina():
    print('1. Limpia')
    print('2. Sucia')
    print('3. Salir')
    op = validarNumero('Digite una opcion valida: ')
    match op:
        case 1:
            proteinaLimpia()
            pass
        case 2:
            proteinaSucia()
            pass
        case 3:
            print('Saliendo de Proteinas')

def creatina():
    print('1. Pastillas')
    print('2. Polvo')
    print('3. Volver al Menu Anterior')
    op = validarNumero('Digite una opcion valida: ')
    match op:
        case 1:
            creatinaPastillas()
            pass
        case 2:
            creatinaPolvo()
            pass
        case 3:
            print('Saliendo de Creatinas')

def preentrenos():
    print('C4')
    print('')
    op = validarNumero('Digite una opcion valida: ')
    match op:
        case 1:
            pass
        case 2:
            pass
        case 3:
            print('Saliendo de Preentrenos')

def suplementosVarios():
    print('1. Tribulus')
    print('2. Magnesio')
    print('3. AnimalPak')
    print('4. Volviendo al Menu Anterior ')
    op = validarNumero('Digite una opcion valida: ')
    match op:
        case 1:
            pass
        case 2:
            pass
        case 3:
            print('1. Animel Pak equivale a 40')
            print('2. Animal Pak completo equivakle a $55')
            op = validarNumero('Digite una opcion valida:')
            match op:
                case 1:
                    print()


def proteinaLimpia():
    print()
    print()
    print()
    print()
    pass

def proteinaSucia():
    print('1. King Mass Ronnie Coleman')
    print()
    print()
    print('Volviendo al Menu Anterior')
    pass

def creatinaPastillas():
    print()
    print()
    print('Volviendo al Menu Anterior')
    pass

def creatinaPolvo():
    print()
    print()
    print('Volviendo al Menu Anterior')
    pass

def Tribulus():
    print()
    print()
    print('Volviendo al Menu Anterior')
    pass

def AnimalPak1():
    animalpak1 = int(input('¿Cuanta cantidad necesita?: '))
    animalpak1 * 40
    