from Persona import Persona
from Empleado import Empleado

class Inicio():
    Cristian=Persona()
    Andres=Persona()
    cristian=Empleado()

    Cristian.pedirDatos()
    Cristian.mostrarDatos()
    print(Cristian.calcularlmc(Cristian.peso))
    Cristian.mayorEdad()
    cristian.calcularHonorarios()
    cristian.imprimirEmpleado()