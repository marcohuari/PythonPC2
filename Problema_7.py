

def es_primo(numero):
    es_primo = True
    for i in range(2,numero):
        if numero%i == 0:
            es_primo = False
            break
    if es_primo:
        rpta = 'Si es primo'
    else:
        rpta = 'No es primo'
    return rpta

print(f"El número {es_primo(100)}")



