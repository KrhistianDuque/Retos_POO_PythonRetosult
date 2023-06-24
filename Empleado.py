
from Persona import Persona

class Empleado(Persona):
    
    
    def __init__(self):
        self.cargo=""
        self.valorHora=0
        self.horastrabajadas=0
        self.departamento=""
        self.total=0

    def calcularHonorarios(self):
        print("Calculo valor de honorarios")
        self.valorHora=int(input("Por favor indique el valor por hora"))
        self.horastrabajadas=int(input("Horas trabajadas"))
        self.total=(self.valorHora*self.horastrabajadas)-0.966*0.01/(self.valorHora*self.horastrabajadas)
        
    def imprimirEmpleado(self):
        print("Su documento es ",self.tipoDoc)
        print("Su nombre es ",self.nombre)
        print("Su nombre es ",self.apellido)
        print("Su valor por hora",self.valorHora)
        print("Su total de honorarios es ",self.total)
    

