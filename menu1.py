from cliente import *
from validaciones import *
from archivo import *
import time_form as t
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

def solicitarProducto(producto_clasificacion):
    dict_producto = loadJSONProduct(producto_clasificacion)
    set_product = v.generateSet(dict_producto, True)
    llave, valor = solicitarValorProducto(dict_producto, set_product)
    if llave is None:
        return
    cantidad = int(input(f'Digite la cantidad para el producto {llave}: '))
    func = lambda valor_producto, cantidad: valor_producto * cantidad
    price = func(valor, cantidad)
    generarFactura(llave, valor, price)

def generarFactura(producto, cantidad, precio):
    global n_factura
    current_time = t.getCurrentTime()
    print(f'Arnold Gym --- {v.showDate(current_time)}')
    print(f'Factura N°{n_factura}\n')
    print(f'{producto} ------ {cantidad}')
    print('\nImpuestos\n')
    print('IVA : 15%')
    total = (precio * cantidad)
    total *= 0.15
    print(f'Pago total: {total}')
    n_factura +=1

def solicitarValorProducto(dict_producto, set_product):
    for producto_in_set in set_product:
        print(f'{producto_in_set} ', end=',')
    print('\n')
    producto = str(input('Digite un producto de la lista: '))
    print(producto)
    for product in dict_producto.keys():
        if product == producto:
            return producto, dict_producto[producto]
    print('Producto no encontrado en la lista.')
    return None, None
    