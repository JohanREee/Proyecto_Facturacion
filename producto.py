from archivo import loadJSONProduct, generateSet,scriptPath
from time_form import getCurrentTime, showDate
from configure import getInfoFromFile,putInfoInFile
from validaciones import validarNumero
import json
n_factura = 1
def n_factura_iterate():
    file = scriptPath('files','facturas.json')
    file_content= getInfoFromFile(file)
    if file_content == None:
        return
    for content in file_content['facturas']:
        n_factura +=1
def solicitarProducto(producto_clasificacion):
    dict_producto = loadJSONProduct(producto_clasificacion)
    set_product = generateSet(dict_producto, True)
    llave, valor = solicitarValorProducto(dict_producto, set_product)
    if llave is None:
        return
    cantidad = validarNumero(f'Digite la cantidad para el producto {llave}: ')
    func = lambda valor_producto, cantidad: valor_producto * cantidad
    price = func(valor, cantidad)
    price += price *0.15
    generarFactura(llave, valor, price)


def generarFactura(producto, cantidad, precio):
    global n_factura
    current_time = getCurrentTime()
    print(f'Arnold Gym --- {showDate(current_time)}')
    print(f'Factura N°{n_factura}\n')
    print(f'{producto} ------ {cantidad}')
    print('\nImpuestos\n')
    print('IVA : 15%')
    print(f'Pago total: {precio}')
    n_factura +=1

def solicitarValorProducto(dict_producto, set_product):
    for producto_in_set in set_product:
        print(f'{producto_in_set}, ', end='')
    print('\n')
    producto = str(input('Digite un producto de la lista: '))
    print(producto)
    for product in dict_producto.keys():
        if product == producto:
            return producto, dict_producto[producto]
    print('Producto no encontrado en la lista.')
    return None, None

def transformBillToJson(fact):
    data = []
    data_client ={
        "Numero de factura" : fact[0],
        "Producto" : fact[1],
        "Cantidad" : fact[2],
        "Precio" : fact[3]
    }
    data.append(data_client)
    return data
def guardarFactura(fact):
    file = scriptPath('files','facturas.json')
    factura_json = transformBillToJson(fact)
    dict_factura = {'factura': factura_json}
    with open(file, 'w') as f:
        json.dump(factura_json, fp=file, indent=4)
    
if __name__ == "__main__":
    pass