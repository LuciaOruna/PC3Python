#ejercicio 2
def obtener_calificaciones():
    while True:
        try:
            # Solicitar al usuario una lista de calificaciones separadas por comas
            calificaciones_str = input("Ingrese las calificaciones separadas por comas: ")
            
            # Dividir la cadena en calificaciones individuales
            calificaciones_lista = calificaciones_str.split(',')
            
            # Convertir cada calificación en un entero
            calificaciones_enteros = [int(calificacion) for calificacion in calificaciones_lista]

            return calificaciones_enteros
        
        except ValueError:
            print("Error: Por favor, ingrese solo números enteros separados por comas.")
            continue

def main():
    calificaciones = obtener_calificaciones()
    print("Calificaciones ingresadas:", calificaciones)

if __name__ == '__main__':
    main()
