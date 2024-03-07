from validaciones import *
from ProductoSubMenu import *
from Asesoramientos import *

def menuPrincipal():
    print('Bienvenido a Arnold Gym')
    print('1. Agregar cliente')
    print('2. Editar cliente')
    print('3. Buscar cliente')
    print('4. Eliminar cliente')
    print('5. Menu de Servicios')
    print('6. Menu de Productos')
    print('7. Menu de Asesoramientos')
    print('8. Menu de Configuracion')
    print('9. Salir')
    op = validarNumero('Digite una opcion valida: ')
    match op:
        case 1:
            print('Agregando cliente')
        case 2:
            print('Editando cliente')
        case 3:
            print('Buscando cliente')
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
