#ejercicio 10
import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

class CUADRADO:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

def mostrar_menu():
    print("\nMenú:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            radio = float(input("Ingrese el radio del círculo: "))
            circulo = CIRCULO(radio)
            print("El área del círculo es:", circulo.calcular_area())
        elif opcion == "2":
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            rectangulo = RECTANGULO(largo, ancho)
            print("El área del rectángulo es:", rectangulo.calcular_area())
        elif opcion == "3":
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = CUADRADO(lado)
            print("El área del cuadrado es:", cuadrado.calcular_area())
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
