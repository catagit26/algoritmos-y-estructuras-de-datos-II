# Materia: Algoritmos y Estructuras de Datos II
# Alumna: Catalina Calderon
# TP N°: 1 | Ejercicio N°: 2
# Fecha de entrega: 15/04/2026
import math ## Importamos la librería matemática para usar el valor preciso de PI
class Figura:
    def __init__(self, color):
        self.color = color

    def area(self):
        return 0 #la base retorna en 0

    def describir(self): #invocamos área () y color para informe
        return f"Figura de color: {self.color}, área calculada de: {self.area()}"

class Rectangulo (Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura #calculamos base por altura

class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2 #calculamos PI multiplicado por el adio elevado al cuadrado
#verificacion polimorfismo
lista_figuras = [ #creamos los objetos dentro de la lista
    Rectangulo("rojo", 10, 5),
    Circulo ("azul", 7)
]
print ("--Informe de Áreas--")
for figura in lista_figuras: #cada objeto responde con su propia fórmula de área
    print(figura.describir())
