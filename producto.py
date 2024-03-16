from archivo import loadJSONProduct, generateSet
from time_form import getCurrentTime, showDate

def solicitarProducto(producto_clasificacion):
    dict_producto = loadJSONProduct(producto_clasificacion)
    set_product = generateSet(dict_producto, True)
    llave, valor = solicitarValorProducto(dict_producto, set_product)
    if llave is None:
        return
    cantidad = int(input(f'Digite la cantidad para el producto {llave}: '))
    func = lambda valor_producto, cantidad: valor_producto * cantidad
    price = func(valor, cantidad)
    generarFactura(llave, valor, price)

def generarFactura(producto, cantidad, precio):
    global n_factura
    current_time = getCurrentTime()
    print(f'Arnold Gym --- {showDate(current_time)}')
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

if __name__ == "__main__":
    pass