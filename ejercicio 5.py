#ejercicio 5
class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de registro:", self.numero_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        else:
            print("Edad: No asignada")
        if self.notas:
            print("Notas:", self.notas)
        else:
            print("Notas: No asignadas")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, notas):
        self.notas = notas

def main():
    # Crear un objeto de la clase Alumno
    alumno1 = Alumno("Juan", "A123")

    # Asignar la edad al estudiante
    alumno1.setAge(20)

    # Asignar las notas al estudiante
    alumno1.setNota([85, 90, 75])

    # Mostrar toda la información del estudiante
    alumno1.display()

if __name__ == '__main__':
    main()
