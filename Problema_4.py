
n = int(input("Digite la cantidad de alumnos en el colegio: "))

lista_alumnos = []

for i in range(n):
    al1 = input(f"Digite el nombre del alumno {i+1}: ")
    n1 = int(input("Digite la nota 1: "))
    n2 = int(input("Digite la nota 2: "))
    n3 = int(input("Digite la nota 3: "))

    lista_notas = []
    lista_notas.append(n1)
    lista_notas.append(n2)
    lista_notas.append(n3)

    diccionario_alumnos = {
                            "Alumnos": al1,
                            "Notas": lista_notas
    }

    lista_alumnos.append(diccionario_alumnos)

print(lista_alumnos)