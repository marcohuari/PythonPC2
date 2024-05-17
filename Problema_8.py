
def fact_num(numero):
    lista = []
    fact = 1
    if numero < 0:
        numero = abs(numero)

    for i in range(numero):
        lista.append(i+1)
    for i in lista:
        fact = fact * i
    return fact

print(fact_num(5))