
flag = True
lista = []
n_pares = 0
n_impares = 0

while flag:
    rpta = input("Desea ingresar un número: ").upper()
    if rpta == 'SI':
        n = int(input("Ingrese el número: "))
        flag = True
        lista.append(n)
    else:
        flag = False

for i in lista:
    if i%2 == 0:
        n_pares = n_pares + 1
    else:
        n_impares = n_impares + 1

print(f"El número de pares es {n_pares} y el número de impares es {n_impares}")
