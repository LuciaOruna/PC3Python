#ejercicio 4
class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

def main():
    try:
        # Solicitar al usuario el largo y el ancho del rectángulo
        largo = float(input("Ingrese el largo del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        
        # Crear un objeto de la clase RECTANGULO
        rectangulo = RECTANGULO(largo, ancho)

        # Calcular y mostrar el área del rectángulo
        area = rectangulo.calcular_area()
        print("El área del rectángulo es:", area)

    except ValueError:
        print("Error: Por favor, ingrese números para el largo y el ancho del rectángulo.")

if __name__ == '__main__':
    main()
