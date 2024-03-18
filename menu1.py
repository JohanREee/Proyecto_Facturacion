from cliente import *
from validaciones import *
from archivo import *
import time_form as t
from producto import *
from sys import exit as ex
n_factura = 1
#dale

def menuPrincipal():
    print('Bienvenido a Arnold Gym')
    print('1. Agregar cliente')
    print('2. Editar cliente')
    print('3. Mostrar cliente')
    print('4. Eliminar cliente')
    print('5. Activar cliente')
    print('6. Mostrar todos los clientes')
    print('7. Menu de Servicios')
    print('8. Menu de Productos')
    print('9. Menu de Asesoramientos')
    print('10. Menu de Configuracion')
    print('11. Salir')
    op = validarNumero('Digite una opcion valida: ')
    match op:
        case 1:
            lista_clientes.append(Cliente())
            saveClient(lista_clientes)
        case 2:
            editarCliente()
            saveClient(lista_clientes)
        case 3:
            cliente = buscarCliente(lista_clientes, setId())
            if cliente is None:
                return
            cliente.showClient()
        case 4:
            triggerClientState('off')
            saveClient(lista_clientes)
        case 5:
            triggerClientState('on')
            saveClient(lista_clientes)
        case 6:
            showAllClients()
        case 7:
            menuServicios()
        case 8:
            menuProductos()
        case 9:
            menuAsesoramientos()
        case 10:
            print('Menu de WU')
        case 11:
            print('Saliendo del programa')
            return 11
        case _:
            print('Valor invalido. Volver a intentar')

def menuServicios():
    while True:
        print('Menu de cuotas')
        print('1. Formato Mensual')
        print('2. Formato Quincenal')
        print('3. Formato Semanal')
        print('4. Formato Diario')
        print('5. Volver a Menu Anterior')
        op = validarNumero('Digite una opcion valida: ')
        match op:
            case 1:
                addService('month')
                saveClient(lista_clientes)
            case 2:
                addService('fortknight')
                saveClient(lista_clientes)
            case 3:
                addService('week')
                saveClient(lista_clientes)
            case 4:
                addService('day')
                saveClient(lista_clientes)
            case 5:
                print('Volviendo al menu anterior')
                return
            case _:
                print('Valor invalido. Volver a intentar')
def menuAsesoramientos():
    while True:
        print("Menu de asesoramientos")
        print("1. Full Arnold")
        print("2. Full Body")
        print("3. Tonificar")
        print("4. Asesoramiento Basico")
        op = validarNumero("Digite una opcion valida: ")
        match op:
            case 1:
                addConsultancy("Full Arnold")
                saveClient(lista_clientes)
            case 2:
                addConsultancy("Full Body")
                saveClient(lista_clientes)
            case 3:
                addConsultancy("Full Tonificar")
                saveClient(lista_clientes)
            case 4:
                addConsultancy("Asesoramiento Basico")
                saveClient(lista_clientes)
            case 5:
                print("Volviendo al menu anterior")
                return
def menuProductos():
    
        print('Menu de productos')
        print('1. Productos Libreados')
        print('2. Productos en Scoops')
        print('3. Productos en Pastillas')
        print('4. Productos en Tarro o Total')
        print('5. Volver a menu Anterior')
        op = validarNumero('Digite una opcion valida: ')
        match op:
            case 1:
                solicitarProducto("Libreados")
            case 2:
                solicitarProducto("Scoops")
            case 3:
                solicitarProducto("Pastilla")
            case 4:
                solicitarProducto("Tarros")
            case 5:
                print('Volviendo al Menu Anterior')
                return

def menuConfiguracion():
    print('1. Editar servicios')
    print('2. Editar productos')
    print('3. Volver al Menu Anterior')
    