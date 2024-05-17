
def conteo_numero(numero,digito):
    lista = []

    for i in str(numero):
        lista.append(i)

    cant = lista.count(str(digito))
    return cant

print(conteo_numero(101123011,1))