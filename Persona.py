import math

class Persona():
    tipoDoc="T.I"
    nombre="Cristian"
    apellido="Duque"
    valorHora="5"
    

    def __init__(self):
        self.tipoDoc=""
        self.documento=0
        self.nombre=""
        self.apellido=""
        self.peso=0
        self.estatura=0.0
        self.edad=0
        self.sexo=""


    def pedirDatos(self):
        self.__tipoDoc=input("Por favor digite su tipo de documento: ")
        self.__documento=int(input("Indique su documento: "))
        self.__nombre=input("Digite su nombre: ")
        self.__apellido=input("Digite su apellido: ")
        self.__peso=float(input("Digite su peso: "))
        self.__estatura=float(input("Digite su estatura: "))
        self.__edad=int(input("Digite su edad: "))
        self.__sexo=input("Digite su genero: ")


    def mostrarDatos(self):
        print("Su tipo de documento es ",self.__tipoDoc)
        print("Su numero de documento es ",self.__documento)
        print("Su nombre es",self.__nombre)
        print("Su apellido es",self.__apellido)
        print("Su peso es de:  ",self.__peso)
        print("Su estatura es de: ",self.__estatura)
        print("Su edad es: ",self.__edad)
        print("Su genero es de_ ",self.__sexo)

    def calcularlmc(self,peso):
        elevacionestatura=math.pow(self.estatura,2)
        pesoActual=peso/elevacionestatura
        conclusion=""
        print("Su imc es de: ",pesoActual)
        if(pesoActual<=20):
           conclusion="El peso esta por debajo de la unidad"
        elif(pesoActual>=20 and pesoActual<=25):
            conclusion="El peso es ideal"
        elif(pesoActual>=25):
            conclusion="Tiene sobrepeso"
        return conclusion

    def mayorEdad(self):
        if(self.edad>18):
            print("Ud es mayor de edad")
        else:
            print("Ud es menor de edad")  



    