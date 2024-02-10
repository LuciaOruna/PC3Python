#ejercicio 8
import random

def generar_numeros():
    return [random.randint(0, 100) for _ in range(20)]

def mostrar_lista(lista):
    print("Lista de números generados:")
    for numero in lista:
        print(numero, end=" ")
    print()

def ordenar_lista(lista):
    lista.sort()
    print("Lista ordenada:")
    for numero in lista:
        print(numero, end=" ")
    print()

if __name__ == "__main__":
    numeros = generar_numeros()
    mostrar_lista(numeros)
    ordenar_lista(numeros)



#Main
import generador_numeros

def main():
    # Generar la lista de números
    lista_numeros = generador_numeros.generar_numeros()

    # Mostrar la lista original
    generador_numeros.mostrar_lista(lista_numeros)

    # Ordenar y mostrar la lista ordenada
    generador_numeros.ordenar_lista(lista_numeros)

if __name__ == "__main__":
    main()

