

texto = input("Digite un texto: ")
new_texto = ""

for i in texto:
    if (i.upper() == 'A' or
        i.upper() == 'E' or 
        i.upper() == 'I' or 
        i.upper() == 'O' or 
        i.upper() == 'U' ):
        new_texto = new_texto + ""
    else:
        new_texto = new_texto + i

print(new_texto)