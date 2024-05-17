
n = int(input("Digite el número a hacer espejo: "))
n_filas = (n*2)-1
lista = []

for j in range(n_filas):
    lista.append(j+1)

for i in lista:
    if i <= n:
        print("*"*i)
    else:
        print("*"*(n_filas-i+1))