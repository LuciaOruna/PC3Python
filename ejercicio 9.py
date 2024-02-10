#ejercicio 9
def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None

def producto(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
        return None
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None

#calculos.py
import operaciones

def main():
    # Ejemplo de uso de las funciones
    print("Suma:", operaciones.suma(10, 5))
    print("Resta:", operaciones.resta(10, 5))
    print("Producto:", operaciones.producto(10, 5))
    print("División:", operaciones.division(10, 5))

if __name__ == "__main__":
    main()
