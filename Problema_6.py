

def suma(n1 = 0,n2 = 0):
    suma = n1 + n2
    return suma

n1 = 0
n2 = 1
lista = []
lista.append(n1)
lista.append(n2)

for i in range(1,50):
    aux = n2
    n2 = suma(n1,n2)
    n1 = aux
    if n2 >= 50:
        break
    lista.append(n2)

print(lista)
