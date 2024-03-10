from menu import *
from menu1 import *
import validaciones as v



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
                setListaLibreados()
            case 2:
                setListaScoops()
            case 3:
                setListaPastillas()
            case 4:
                setListaTarros()
            case 5:
                print('Volviendo al Menu Anterior')
                return