#Problema 1:
def obtener_porcentaje(f):
    try:
        # Separar el numerador y el denominador
        numerador, denominador = map(int, f.split('/'))
        
        # Verificar si X e Y son números enteros y Y no es cero
        if numerador <= 0 or denominador <= 0:
            raise ValueError("X e Y deben ser números enteros positivos")

        # Verificar si X es menor o igual a Y
        if numerador > denominador:
            raise ValueError("X debe ser menor o igual a Y")

        # Calcular el porcentaje
        porcentaje = (numerador / denominador) * 100
        
        # Redondear al entero más cercano
        porcentaje_redondeado = round(porcentaje)

        # Determinar la respuesta según el porcentaje
        if porcentaje_redondeado < 1:
            return 'E'
        elif porcentaje_redondeado > 99:
            return 'F'
        else:
            return str(porcentaje_redondeado) + '%'
    
    except ValueError as e:
        print("Error:", e)
        return None
    except ZeroDivisionError:
        print("Error: El denominador no puede ser cero")
        return None

def main():
    while True:
        f = input("Ingrese una fracción en formato X/Y: ")
        resultado = obtener_porcentaje(f)
        if resultado:
            print("Cantidad de combustible en el tanque:", resultado)
            break

if __name__ == '__main__':
    main()
