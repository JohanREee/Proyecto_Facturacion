import validaciones as v
import mensualidad as m
import time_form as t
from os import path
import json as j
from archivo import scriptPath
from asesoramientos import generarAsesoramiento

conteo_cliente = 1
lista_clientes = []
def modificarListaEmpleado(cliente_update, id_cliente):
    for x, cliente in enumerate(lista_clientes):
        if id_cliente == cliente.getIdClient():
            lista_clientes[x] = cliente_update
            
class Cliente:
    def __init__(self, load = None):
        global conteo_cliente
        if load is None:
            self.nombre_completo = v.validarCadena('Digite el nombre del cliente: ')
            self.edad = v.validarNumero('Digite la edad del cliente: ')
            self.__cedula = v.validarCedula('Digite la cedula del cliente: ', lista_clientes)
            self.__servicios = {"Servicios_activos": [], "Asesoramientos_activos": []}        
            self.__id_cliente = conteo_cliente
            self.__band = True
            self.mensualidad_dias = 0 
            self.asesoramiento_dias = 0
            conteo_cliente +=1
            print(f'Usuario {self.nombre_completo} agregado con exito.\n\n')
            return
        self.nombre_completo = load['Nombre completo']
        self.edad = load['Edad']
        self.__cedula = load['Cedula']
        services = load['Servicios']
        self.__servicios = {"Servicios_activos" : loadServices(services), 
                            "Asesoramientos_activos": loadCounseling(services)}
        self.__id_cliente = load['ID']
        conteo_cliente +=1
        self.__band = False if load['Band'] == 'False' else True
        self.mensualidad_dias = 30
        self.asesoramiento_dias = load['Dias de asesoramientos']
        self.mensualidad_dias = load['Dias de mensualidad']
        return
    def getServices(self):
        return self.__servicios
    def getBand(self):
        return self.__band
    
    def getId(self):
        return self.__cedula
    
    def getIdClient(self):
        return self.__id_cliente
    
    def getName(self):
        return self.nombre_completo
    
    def getServices(self):
        return self.__servicios

    def getAge(self):
        return self.edad
    def updateServices(self):
        for mensualidad in self.__servicios["Servicios_activos"]:
            if t.validateTime(mensualidad[2]):
                match mensualidad[0]: 
                    case 'Mensual':
                        self.mensualidad_dias -=30
                    case 'Quincenal':
                        self.mensualidad_dias -=15
                    case 'Semanal':
                        self.mensualidad_dias -=7
                    case 'Diario':
                        self.mensualidad_dias -=1
                del mensualidad

        for asesoramiento in self.__servicios["Asesoramientos_activos"]:
            if t.validateTime(asesoramiento[2]):
                self.asesoramiento_dias -=30
                del asesoramiento

    def showClient(self, bypass = False):#bypass = True for showing ALL clients without asking
        if bypass or self.getBand() == False:
            if not(v.ask('Este usuario ha sido eliminado del sistema. Desea mostrarlo?')):
                return
        print(f'\nNombre: {self.nombre_completo}')
        print(f'Edad: {self.edad}')
        print(f'Cedula: {self.getId()}')
        print(f'ID del cliente: {self.getIdClient()}')
        print(f'Estado: {'Activo' if self.getBand() == True else 'Inactivo'}')
        print('Servicios activos: ')
        self.showMonthlyPayment()
        print("Asesoramientos activos: ")
        self.showConsultancies()
    def showMonthlyPayment(self):
        for mensualidad in self.__servicios["Servicios_activos"]:
            print(f'Tipo de pago: {mensualidad[0]}')
            print(f'Cantidad a pagar: C${mensualidad[1]}')
            print(f'Fecha de expiracion: {t.showDate(mensualidad[2])}\n')
    def showConsultancies(self):
        for asesoramiento in self.__servicios["Asesoramientos_activos"]:
            print(f'Tipo de asesoramiento: {asesoramiento[0]}')
            print(f"Cantidad a pagar: ${asesoramiento[1]}")
            print(f"Fecha de expiracion: {t.showDate(asesoramiento[2])}")
    def editName(self):
        nombre = v.validarCadena('Digite el nuevo nombre del cliente: ')
        print(f'El nombre {self.nombre_completo} ha sido modificado por {nombre}')
        return nombre
    def editAge(self):
        edad = v.validarNumero('Digite la nueva edad del cliente: ', age=True)
        print(f'La edad {self.edad} ha sido modificada por {edad}')
        return edad
    def editClient(self, edit):
        match edit:
            case  1:
                self.nombre_completo = self.editName()
            case  2:
                self.edad = self.editAge()

    def offBand(self):
        self.__band = False
    def onBand(self):

        self.__band = True
    def addService(self, type_of_payment):
        list_payment, self.mensualidad_dias = m.generarMembresia(type_of_payment,self.mensualidad_dias)
        self.__servicios['Servicios_activos'].append(list_payment)

    def addConsultancy(self, type_of_consultancy):
        list_consultancy, self.asesoramiento_dias = generarAsesoramiento(type_of_consultancy, self.asesoramiento_dias)
        self.__servicios['Asesoramientos_activos'].append(list_consultancy)
        
def digitarCedula():
    cedula = str(input('Digite la cedula que desea buscar: '))
    return cedula

def setId():
    return {cliente.getId() for cliente in lista_clientes}

def buscarCliente(lista_cliente, set, cedula = True):
    if cedula:
        cedula = digitarCedula()
    if not (cedula in set):
        print('Cliente no encontrado en el sistema')
        return None
    for cliente in lista_cliente:
        if cedula == cliente.getId():
            return cliente

def editarCliente():
    cliente = buscarCliente(lista_clientes, setId())
    if  cliente is None:
        print('Cliente no encontrado. Volviendo al menu anterior')
        return
    print(f'Opciones a editar para el cliente{cliente.nombre_completo}:')
    print('1.Nombre\n2.Edad\n3. Cedula')
    op = v.validarNumero('Seleccione una opcion valida: ')
    cliente.editClient(op)
    print('Cliente editado exitosamente')

def triggerClientState(action):
    found_client = buscarCliente(lista_clientes, setId())
    if found_client is None:
        print('Cliente no encontrado. Volviendo al menu anterior')
        return
    if found_client.getBand() == False and action == 'off':
        print('No puedes eliminar a un cliente ya eliminado.')
        return
    if found_client.getBand() == True and action == 'on':
        print('No puedes reactivar a un cliente ya activado.')
        return
    
    eliminate_or_activate = 'eliminar' if action == 'off' else 'activar'
    if not(v.ask(f'Estas seguro de querer {eliminate_or_activate} al usuario {found_client.getName()}?')):
        return
    
    for x, current_client in enumerate(lista_clientes):
        if current_client.getId() == found_client.getId():
            if eliminate_or_activate == 'eliminar':
                lista_clientes[x].offBand()
                print('Cliente eliminado del sistema satisfactoriamente')
                return
            lista_clientes[x].onBand()
            print('Cliente reactivado satisfactoriamente')
            return
        
def updateAllClients():
    for cliente in lista_clientes:
        cliente.updateServices()

def addService(type_of_payment):
    cliente = buscarCliente(lista_clientes, setId())
    if cliente is None:
        return
    for x, current_client in enumerate(lista_clientes):
        if current_client.getId() == cliente.getId():
            lista_clientes[x].addService(type_of_payment)
            print(f'Servicio agregado con exito al usuario {cliente.getName()}')
            return

def addConsultancy(type_of_consultancy):
    cliente = buscarCliente(lista_clientes, setId())
    if cliente is None:
        return
    for x, current_client in enumerate(lista_clientes):
        if current_client.getId() == cliente.getId():
            lista_clientes[x].addConsultancy(type_of_consultancy)
            print(f'Asesoramiento agregado con exito al usuario {cliente.getName()}')
            return
        
def showAllClients():
    for cliente in lista_clientes: 
        cliente.showClient(bypass = True)

def transformDateToJson(date):
    return {
        "Year": date[2],
        'Mes' : date[1],
        'Dia' : date[0]
    }

def transformCounTToJson(service):
    data= []
    for serv in service:
        data_s = {
            'Tipo de asesoramiento' : serv[0],
            'Pago' : serv[1],
            'Fecha' : transformDateToJson(serv[2])
        }
        data.append(data_s)
    return data
    
def transformServiceToJson(service):
    data = []
    for serv in service:
        data_s = {
            'Tipo de mensualidad' : serv[0],
            'Pago' : serv[1],
            'Fecha' : transformDateToJson(serv[2])
        }
        data.append(data_s)
    return data
def transformServicesToJson(services):
    services_cliente = {
        "Servicios activos" : transformServiceToJson(services['Servicios_activos']),
        "Asesoramientos" : transformCounTToJson(services["Asesoramientos_activos"])
    }
    return services_cliente
def transformClientsToJson(lista_clientes):
    data = []
    conteo = 1
    for cliente in lista_clientes:
        data_client = [{
            "Nombre completo" : cliente.getName(),
            "Edad" : cliente.getAge(),
            "Cedula" : cliente.getId(),
            "Servicios" : transformServicesToJson(cliente.getServices()),
            "ID" : cliente.getIdClient(),
            "Band" : 'False' if cliente.getBand() == False else 'True',
            "Dias de mensualidad" : cliente.mensualidad_dias,
            "Dias de asesoramientos" : cliente.asesoramiento_dias
        }]
        data.append(data_client)
    return data_client

def saveClient(lista_clientes):
    data = transformClientsToJson(lista_clientes)
    dict = {'clientes' : data}
    file = scriptPath('files', 'clientes.json')
    with open(file, 'w') as f:
        f.write(j.dumps(dict, indent=4))

def loadDate(data):
    return [data['Year'], data['Mes'], data['Dia']]

def loadCounseling(data):
    list = []
    counseling = data['Asesoramientos']
    for c in counseling:
        asesoramiento = c['Tipo de asesoramiento']
        pago = c['Pago']
        fecha = loadDate(c['Fecha'])
        list.append([asesoramiento,pago,fecha])
    return list
def loadServices(data):
    list = []
    monthly_payment = data['Servicios activos']
    for d in monthly_payment:
        mensualidad = d['Tipo de mensualidad']
        precio = d['Pago']
        fecha = loadDate(d['Fecha'])
        list.append([mensualidad, precio, fecha])
    return list
def loadClient():
    file = scriptPath('files', 'clientes.json')
    if not(path.exists(file)):
        return None
    with open(file, 'r') as f:
        data = j.load(f)
    return data
    
def loadAllClients():
    data = loadClient()
    if data is None:
        return
    for cliente in data['clientes']:
        lista_clientes.append(Cliente(load=cliente))

if __name__ == "__main__":
    pass