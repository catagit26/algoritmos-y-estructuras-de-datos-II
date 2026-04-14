# Materia: Algoritmos y Estructuras de Datos II
# Alumna: Catalina Calderon
# TP N°: 1 | Ejercicio N°: 1
# Fecha de entrega: 15/04/2026
class Vehiculo: #clase base
    def __init__ (self, marca, velocidad_max):
        # constructor: se ejecuta al crear el objeto para asignarle sus datos iniciales
        self.marca = marca
        self.velocidad_max = velocidad_max
    def describir (self): #metodo
        return f"Marca del vehículo: {self.marca}, Velocidad máxima: {self.velocidad_max} km/h"
        # "return" devuelve el texto armado para que se pueda usar o imprimir afuera
    # f-string: combina atributos del objeto ({self.""}) directamente en el texto

class Auto (Vehiculo): #clase hija
    def __init__ (self, marca, velocidad_max, puertas ):
        super().__init__ (marca, velocidad_max)
        # llama al constructor del padre para reutilizar su lógica
        self.puertas = puertas
    def describir (self):
        return f"Marca del auto: {self.marca}, Alcanza: {self.velocidad_max} km/h, Cantidad de puertas: {self.puertas }"

class Moto (Vehiculo):
    def __init__ (self, marca, velocidad_max, cilindrada ):
        super().__init__ (marca, velocidad_max)
        self.cilindrada = cilindrada
    def describir (self):
        return f"Marca de la Moto: {self.marca}, Tope de velocidad: {self.velocidad_max} km/h, Cilindrada: {self.cilindrada}"

auto = Auto("Fiat", 180, 5)
moto = Moto("Yamaha", 120, "250cc")
#creamos los objetos
lista_vehiculos = [auto, moto]
#metemos los objetos en una lista
print("-- Informe de Vehículos --")
for vehiculo in lista_vehiculos: 
    print(vehiculo.describir())
#polimorfismo -> solo llamamos a describir() y python sabe que elegir
