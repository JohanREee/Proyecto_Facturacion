from cliente import *
from validaciones import *
from archivo import *
import time_form as t
lista_productos_libreados = []
lista_productos_scoops = []
lista_productos_pastillas = []
lista_productos_tarros = []
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
        case 2:
            editarCliente()
        case 3:
            cliente = buscarCliente(lista_clientes, setId())
            if cliente is None:
                return
            cliente.showClient()
        case 4:
            triggerClientState('off')
        case 5:
            triggerClientState('on')
        case 6:
            showAllClients()
        case 7:
           menuServicios()
        case 8:
             menuProductos()
        case 9:
           print('Menu de asesormamientos WU')
        case 10:
             print('Menu de configuracion WU')
        case 11:
            #codigo para guardar datos en un archivo
            exit('Saliendo del programa')
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
            case 2:
                addService('fortknight')
            case 3:
                addService('week')
            case 4:
                addService('day')
            case 5:
                print('Volviendo al menu anterior')
                return
            case _:
                print('Valor invalido. Volver a intentar')

def menuProductos():
    
        print('Menu de productos')
        print('1. Productos Libreados')
        print('2. Productos en Scoops')
        print('3. Productos en Pastillas')
        print('4. Productos en Tarro o Total')
        print('5. Volver a Menu Anterior')
        op = validarNumero('Digite una opcion valida: ')
        match op:
            case 1:
                solicitarProducto('Productos_libreados')
            case 2:
                solicitarProducto('Productos_scoops')
            case 3:
                solicitarProducto('Productos_pastillas')
            case 4:
                solicitarProducto('Productos_Tarros_Total')
            case 5:
                print('Volviendo al Menu Anterior')
                return
            
def solicitarProducto(producto_clasificacion):
    set_producto = loadJSONProduct(producto_clasificacion)
    for producto in set_producto:
        print(producto, end=',')
    print('\n')
    producto = str(input('Digite un producto de la lista: '))
    if not(producto in set_producto):
        print('Producto no encontrado. Volviendo al menu anterior')
        return
    x = None
    match producto_clasificacion:
        case 'Productos_libreados':
            x = 'libras'
        case 'Productos_scoops':
            x = 'scoops'
        case 'Productos_pastillas':
            x = 'pastillas'
        case 'Productos_Tarros_Total':
            x = 'tarros'
    cantidad = validarNumero(f'Digite la cantidad de {x} que desea: ')

''''
def setListaPastillas():
    return {producto for producto in lista_productos_pastillas}
def solicitarProducto():
    set_lista_pastillas = setListaPastillas()
    for producto in set_lista_pastillas:
        print(producto, end=',')
    print('\n')

    producto = str(input('Digite un producto de la lista: '))
    if not(producto in set_lista_pastillas):
        print('Producto no encontrado. Volviendo al menu anterior')
        return
    
    libra = str(input(f'Digite la cantidad de libras para el producto {producto}: '))


def setListaTarros():
    return {producto for producto in lista_productos_tarros}
def solicitarProducto():
    set_lista_tarros = setListaTarros()
    for producto in set_lista_tarros:
        print(producto, end=',')
    print('\n')

    producto = str(input('Digite un producto de la lista: '))
    if not(producto in set_lista_tarros):
        print('Producto no encontrado. Volviendo al menu anterior')
        return
    
    libra = str(input(f'Digite la cantidad de libras para el producto {producto}: '))
'''