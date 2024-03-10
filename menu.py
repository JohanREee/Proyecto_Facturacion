from cliente import *
from validaciones import *
from asesoramientos import *
#start of ProductoSubMenu.py


def MenuProteinas():
    while True:
        print('1. Limpia')
        print('2. Sucia')
        print('3. Salir')
        op = validarNumero('Digite una opcion valida: ')
        match op:
            case 1:
                proteinaLimpia()
            
            case 2:
                proteinaSucia()
            
            case 3:
                print('Saliendo de Proteinas')
                break

def MenuCreatinas():
    while True:
        print('1. Pastillas')
        print('2. Polvo')
        print('3. Volver al Menu Anterior')
        op = validarNumero('Digite una opcion valida: ')
        match op:
            case 1:
                creatinaPastillas()
            case 2:
                creatinaPolvo()
            case 3:
                print('Saliendo de Creatinas')
                break

def C4():
    C4 = int(input('¿Cuantos scoops necesita?: '))
    C4 * 45

def Psychotic():
    Psychotic = int(input('¿Cuantos scoops necesita?: '))
    Psychotic * 50

def MicronizedLGlutamine():
    MicronizedLGlutamine = int(input('¿Cuantos scoops necesita?: '))
    MicronizedLGlutamine * 45

def MenuPreEntrenos():
    while True:
     print('1. C4')
     print('2. Psychotic')
     print('3. Micronized L Glutamine')
     print('4. Regresar al Menu anterior')
     op = validarNumero('Digite una opcion valida: ')
     match op:
        case 1:
            while True:
                print('1. Scoops de C4')
                print('2. Tarro Completo')
                print('3. Volver al Menu Anterior')
                op = validarNumero('Digite una opcion valida: ')
                match op:
                    case 1:
                        C4()
                    case 2:
                        print(1500, 'Precio del Tarro Completo')
                    case 3:
                        print('Volviendo al Menu Anterior')
                        break
        case 2:
            while True:
                print('1. Scoops de Psychotic')
                print('2. Tarro Completo')
                print('3. Volver al Menu Anterior')
                op = validarNumero('Digite una opcion valida: ')
                match op:
                    case 1:
                        Psychotic()
                    case 2:
                        print(1600, 'Precio del Tarro Completo')
                    case 3: 
                        print('Volviendo al Menu Anterior')
                        break
        case 3:
            while True:
             print('1. Scoops de MicronizedLGlutamine')
             print('2. Tarro Completo')
             print('3. Volver al Menu Anterior')
             op = validarNumero('Digite una opcion valida: ')
             match op:
                case 1:
                    MicronizedLGlutamine()
                case 2:
                    print(1550, 'Precio del Tarro Completo')
                case 3:
                    print('Volviendo al Menu Anterior')
                    break
        case 4:
            print('Saliendo de Preentrenos')
            break

def AnimalPak1():
    animalpak1 = int(input('¿Cuanta cantidad necesita?: '))
    animalpak1 * 40

def TribulusRN():
    TribulusRN = int(input('¿Cuanta cantidad necesita?: '))
    TribulusRN * 10

def TribulusMyProtein():
    TribulusMyProtein = int(input('¿Cuanta cantidad necesita?: ')) 
    TribulusMyProtein * 11

def Tribulus():
    while True:
        print('1. Tribulus Ronnie Coleman')
        print('2. Tribubulus MyProtein')
        print('Volviendo al Menu Anterior')
        op = validarNumero('Digite una opcion valida: ')
        match op:
            case 1:
                while True:
                    print('1. Capsula de Tribulus Ronnie Coleman')
                    print('2. Tarro Completo')
                    print('3. Volver al Menu Anterior')
                    op = validarNumero('Digite una opcion valida: ')
                    match op:
                        case 1:
                            TribulusRN()
                        case 2:
                            print(720, 'Precio del Tarro Completo')
                        case 3:
                            print('Volviendo al Menu Anterior')
                            break
            case 2:
                while True:
                    print('1. Capsula de Tribulus My Protein')
                    print('2. Tarro Completo')
                    print('3. Volver al Menu Anterior')
                    op = validarNumero('Digite una opcion valida: ')
                    match op:
                        case 1:
                            TribulusMyProtein()
                        case 2:
                            print(800, 'Precio del Tarro Completo')
                        case 3:
                            print('Volver al Menu Anterior')
                            break
            case 3:
                print('Volviendo al Menu Anterior')
                break

                
    

def MenuSuplementosVarios():
    while True:
        print('1. Tribulus')
        print('2. Magnesio')
        print('3. AnimalPak')
        print('4. Volver al Menu Anterior ')
        op = validarNumero('Digite una opcion valida: ')
        match op:
            case 1:
                Tribulus()
            case 2:
                while True:
                    print('1. Valor de Barra de Magnesio')
                    print('2. Volver al Menu Anterior')
                    op = validarNumero('Digite una opcion valida: ')
                    match op:
                        case 1:
                            print(200, '1. Valor de Barra de Magnesio')
                        case 2:
                            print('Volviendo al Menu Anterior')
                            break

            case 3:
                while True:
                    print('1. Sobre Animel Pak equivale a 40')
                    print('2. Animal Pak completo equivale a 1950')
                    print('3,. Volver al Menu Anterior')
                    op = validarNumero('Digite una opcion valida:')
                    match op:
                        case 1:
                            AnimalPak1()
                        case 2:
                            print(1950, 'Gracias por su adquisicion')
                        case 3:
                            print('Volviendo al Menu Anterior')
                            break
            case 4:
                print('Volviendo al Menu Anterior')
                break

                    
def WheyProteinEVL():
    WheyProteinEVL = int(input('¿Cuanta cantidad necesita?: '))
    WheyProteinEVL * 460
    

def IsolateProteinRule1():
     IsolateProteinRule1 = int(input('¿Cuanta cantidad necesita?: '))
     IsolateProteinRule1 * 440

def WheyProteinRonnieColeman():
    WheyProteinRonnieColeman = int(input('¿Cuanta cantidad necesita?: '))
    WheyProteinRonnieColeman * 455


def proteinaLimpia():
    print('Todas las proteinas son vendidas por libra')
    print('En caso de bolson hablar por privado')
    print('1. Whey Protein EVL')
    print('2. Isolate Protein Rule 1')
    print('3. Whey Protein Ronnie Coleman')
    print('4. Volver al Menu Anterior')
    op = validarNumero('Digite una opcion valida: ')
    match op:
        case 1:
            WheyProteinEVL()
        case 2:
            IsolateProteinRule1()
        case 3:
            WheyProteinRonnieColeman()
        case 4:
            print('Volviendo al Menu Anterior')

def KingMassRonnieColeman():
    KingMassRonnieColeman = int(input('¿Cuanta cantidad necesita?: '))
    KingMassRonnieColeman * 240

def DymatizeMassGainer():
     DymatizeMassGainer = int(input('¿Cuanta cantidad necesita?: '))
     DymatizeMassGainer * 250

def Rule1MassGainer():
    Rule1MassGainer = int(input('¿Cuanta cantidad necesita?: '))
    Rule1MassGainer * 255

def proteinaSucia():
    print('Todas las proteinas son vendidas por libra')
    print('En caso de bolson hablar por privado')
    print('1. King Mass Ronnie Coleman')
    print('2. Dymatize Mass Gainer')
    print('3. Rule 1 Mass Gainer Protein')
    print('4. Volver al Menu Anterior')
    op = validarNumero('Digite una opcion valida: ')
    match op:
        case 1:
            KingMassRonnieColeman()
        case 2:
            DymatizeMassGainer()
        case 3:
            Rule1MassGainer()
        case 4:
            print('Volviendo al Menu Anterior')

def ONCreatineCapsules():
    OnCreatineCapsules = int(input('¿Cuanta cantidad necesita?: '))
    OnCreatineCapsules * 40

def EVLCreatine1000():
    EVLCreatine1000 = int(input('¿Cuanta cantidad necesita?: '))
    EVLCreatine1000 * 40

def creatinaPastillas():
    print('Solamente se dan su venta por su unidad')
    print('En caso de necesitar tarro hablar por privado')
    print('1. ONC Creatine Capsules')
    print('2. EVL Creatine 1000 Capsule')
    print('3. Volver al Menu Anterior')
    op = validarNumero('Digite una opcion valida: ')
    match op:
        case 1:
            ONCreatineCapsules()
        case 2:
            EVLCreatine1000()
        case 3:
            print('Volviendo al Menu Anterior')

def CreatinaRN():
    CreatinaRN = int(input('¿Cuantos scoops necesita?: '))
    CreatinaRN * 23

def CreatinaMuscleTech():
    CreatinaMuscleTech = int(input('¿Cuantos scoops necesita?: '))
    CreatinaMuscleTech * 25

def CreatinaRightNutrition():
    CreatinaRightNutrition = int(input('¿Cuantos scoops necesita?: '))
    CreatinaRightNutrition * 20

def CreatinaRule1():
    CreatinaRule1 = int(input('¿Cuantos scoops necesita?: '))
    CreatinaRule1 * 22

def creatinaPolvo():
    print('1. Ronnie Coleman Creatine')
    print('2. MuscleTech Creatine 5000')
    print('3. Right Nutrition Creatine Drive')
    print('4. Rule 1 Creatine 1000')
    print('4. Volver al Menu Anterior')
    op = validarNumero('Digite una opcion valida: ')
    match op:
        case 1:
            print('1. Scoops de Creatina Ronnie Coleman')
            print('2. Tarro Completo')
            op = validarNumero('Digite una opcion valida: ')
            match op:
                case 1:
                    CreatinaRN()
                case 2:
                    print(1100, 'Precio del Tarro Completo')
        case 2:
            print('1. Scoops de Creatina MuscleTech')
            print('2. Tarro Completo')
            op = validarNumero('Digite una opcion valida: ')
            match op:
                case 1:
                    CreatinaMuscleTech()
                case 2:
                    print(1200, 'Precio del Tarro Completo')
        case 3:
            print('1. Scoops de Creatina Right Nutrition')
            print('2. Tarro Completo')
            op = validarNumero('Digite una opcion valida: ')
            match op:
                case 1:
                    CreatinaRightNutrition()
                case 2:
                    print(950, 'Precio del Tarro Completo')
        case 4:
            print('1. Scoops de Creatina Rule 1 1000')
            print('2. Tarro Completo')
            op = validarNumero('Digite una opcion valida: ')
            match op:
                case 1:
                    CreatinaRule1()
                case 2:
                    print(1000, 'Precio del Tarro Completo')
            
        case 3:
            print('Volviendo al Menu Anterior')



#End of submenu

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
            print('Mensualidad - 30 dias')
        case 2:
            print('Quincenal - 15 dias')
        case 3:
            print('Semanal - 7 dias')
        case 4:
            print('Diario')
        case 5:
            print('Volviendo al menu anterior')
            return

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
                MenuProteinas()
            case 2:
                MenuCreatinas()
            case 3:
                MenuPreEntrenos()
            case 4:
                MenuSuplementosVarios()
            case 5:
                print('Volviendo al Menu Anterior')
                return

def menuAsesoramientos():
        while True:
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
                    print('Volviendo al Menu Anerior')
                    return 


def menuConfiguracion():
    print('Menu de configuracion')


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
            triggerEliminarCliente()
        case 5:
            triggerActivarCliente()
        case 6:
            menuServicios()
        case 7:
            menuProductos()
        case 8:
            menuAsesoramientos()
        case 9:
            menuConfiguracion()
        case 10:
            #codigo para guardar datos en un archivo
            exit('Saliendo del programa')
        case _:
            print('Valor invalido. Volver a intentar')
