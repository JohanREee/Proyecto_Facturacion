from archivo import loadJSONMonthlyPayment, scriptPath
from validaciones import validarCadena, validarNumero , decoratorvalidate, ask
from json import load, dumps, JSONDecodeError
import os

def getInfoFromFile(*dirs):
    file = scriptPath(*dirs)
    if not(os.path.exists(file)):
        with open(file,'w') as f:pass

    try:
        with open(file,'r') as f:
            file_content = load(f)
    except JSONDecodeError:
        file_content = None
    return file_content

def putInfoInFile(file_content, *dirs):
    file = scriptPath(*dirs)
    with open (file, 'w') as f:
        f.write(dumps(file_content, indent=4))
def chooseMonthlyPayment():
    prices = loadJSONMonthlyPayment()
    while True:
        print("Opciones validas. A la derecha se muestra su precio actual")
        print(f"1. Mensualidad --- {prices[0]}")
        print(f"2. Quincena --- {prices[1]}")
        print(f"3. Semana --- {prices[2]}")
        print(f'4. Dia --- {prices[3]}')
        print("5. Cancelar")
        op = validarNumero('Digite una opcion valida: ')
        match op:
            case 1:
                return 'Monthly'
            case 2:
                return 'Fortknight'
            case 3:
                return 'Week'
            case 4:
                return 'Daily'
            case 5:
                print("Accion cancelada")
                return None
            case _:
                print('Valor invalido. Volver a intentar')

@decoratorvalidate
def askForChange():
    new_price = validarNumero("Digite el nuevo precio que va a tener este parametro: ")
    if new_price <=0:
        raise ValueError
    return new_price

def changePriceOfMonthlyPayment():
    parameter = chooseMonthlyPayment()
    if parameter is None:
        return
    file_content = getInfoFromFile('files', 'mensualidad.json')
    for content in file_content:
        if parameter == content:
            file_content[content] = askForChange()
            break
    putInfoInFile(file_content, 'files', 'mensualidad.json')
    print("Dato modificado exitosamente.")

def chooseCategory():
    while True:
        print("Categorias validas de productos")
        print('1. Libreados')
        print('2. Pastilla')
        print('3. Scoops')
        print('4. Tarros')
        print('5. Cancelar')
        op = validarNumero('Digite una opcion valida: ')
        match op:
            case 1:
                return 'Libreados'
            case 2:
                return 'Pastilla'
            case 3:
                return 'Scoops'
            case 4:
                return 'Tarros'
            case 5:
                print("Accion cancelada")
                return None
            case _:
                print('Valor invalido. Volver a intentar')


def typeProduct():
    producto = validarCadena('Digite el nombre del producto: ')
    return producto

@decoratorvalidate
def priceProduct():
    precio = validarNumero('Digite el precio del producto: ')
    if precio <0:
        raise ValueError
    return precio

def addProduct():
    category = chooseCategory()
    if category is None:
        return
    file_content = getInfoFromFile('files','nombre_productos.json')
    products = file_content[category]
    dict = {typeProduct() : priceProduct()}
    products.update(dict)
    file_content[category] = products
    putInfoInFile(file_content, 'files','nombre_productos.json')
    print("Producto agregado al sistema exitosamente")

@decoratorvalidate
def askForPrice(message):
    price = int(input(message))
    if price <0:
        raise ValueError
    return price
def askForProduct(message):
    product = str(input(message))
    return product

def editOrDeleteProduct(action): #modificar o eliminar
    category = chooseCategory()
    if category is None:
        return
    file_content = getInfoFromFile('files','nombre_productos.json')
    dict_category_loaded = file_content[category]

    for product in dict_category_loaded:
        print(f'{product}', end=', ')

    user_product = askForProduct(f'\nDigite el producto que desea {action}: ')
    for products in dict_category_loaded:
        if products == user_product:
            if action == 'modificar':
                editProduct(dict_category_loaded, products,category, file_content)
                return
            if not(ask(f'Desea eliminar el producto {products}? ')):
                return None
            deleteProduct(dict_category_loaded, products,category, file_content)
            return
    print('No se ha encontrado el producto')
    return

def editProduct(dict_category_loaded, products,category, file_content):
    dict_category_loaded[products] = askForPrice('Digite el nuevo valor del producto: ')
    file_content[category] = dict_category_loaded
    print('Producto editado')
    putInfoInFile(file_content, 'files', 'nombre_productos.json')
    

def deleteProduct(dict_category_loaded, products,category, file_content):
    del dict_category_loaded[products]
    file_content[category] = dict_category_loaded
    print("Producto eliminado")
    putInfoInFile(file_content, 'files', 'nombre_productos.json')
    

        

