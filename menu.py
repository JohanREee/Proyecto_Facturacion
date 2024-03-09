from cliente import *
from validaciones import *
#start of ProductoSubMenu.py


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
    
#end of ProductoSubMenu.py
    
def menuPrincipal():
    print('Bienvenido a Arnold Gym')
    print('1. Agregar cliente')
    print('2. Editar cliente')
    print('3. Mostrar cliente')
    print('4. Eliminar cliente')
    print('5. Activar cliente')
    print('6. Menu de Servicios')
    print('7. Menu de Productos')
    print('8. Menu de Asesoramientos')
    print('9. Menu de Configuracion')
    print('10. Salir')
    op = validarNumero('Digite una opcion valida: ')
    match op:
        case 1:
            lista_clientes.append(Cliente())
        case 2:
            editarCliente()
        case 3:
            cliente = buscarCliente(lista_clientes, setId())
            if cliente is None:
                return
            cliente.showClient()
        case 4:
            print('Eliminando cliente')
        case 5:
            menuServicios()
        case 6:
            menuProductos()
        case 7:
            menuAsesoramientos()
        case 8:
            menuConfiguracion()
        case 9:
            #codigo para guardar datos en un archivo
            exit('Saliendo del programa')
        case _:
            print('Valor invalido. Volver a intentar')
    
def menuServicios():
    print('Menu de cuotas')
    print('1. Formato Mensual')
    print('2. Formato Quincenal')
    print('3. Formato Semanal')
    print('4. Formato Diario')
    print('5. Volver a Menu Anterior')
    op = validarNumero('Digite una opcion valida: ')
    match op:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass

def menuProductos():
    print('Menu de productos')
    print('1. Proteinas')
    print('2. Creatina')
    print('3. Pre entrenos')
    print('4. Suplementos varios')
    print('5. Volver a Menu Anterior')
    op = validarNumero('Digite una opcion valida: ')
    match op:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass

def menuAsesoramientos():
    print('Menu de asesoramientos')
    print('1. Full Arnold')
    print('2. Full Body')
    print('3. Tonificar')
    print('4. Asesoramiento basico')
    print('5. Volver a Menu Anterior')
    op = validarNumero('Digite una opcion valida: ')
    match op:
        case 1:
            FullArnold()
        case 2:
            FullBody()
        case 3:
            Tonificar()
        case 4:
            AsesoramientoBasico()
        case 5:
            pass
        
def menuConfiguracion():
    print('Menu de configuracion')
