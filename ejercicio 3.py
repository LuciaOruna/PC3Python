#ejercicio 3
import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

def main():
    try:
        # Solicitar al usuario el radio del círculo
        radio = float(input("Ingrese el radio del círculo: "))
        
        # Crear un objeto de la clase CIRCULO
        circulo = CIRCULO(radio)

        # Calcular y mostrar el área del círculo
        area = circulo.calcular_area()
        print("El área del círculo es:", area)

    except ValueError:
        print("Error: Por favor, ingrese un número para el radio del círculo.")

if __name__ == '__main__':
    main()
