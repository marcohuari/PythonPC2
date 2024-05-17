

fecha = input("Digite la fecha en formato mm/dd/yyyy o mmm dd, yyyy: ")
lista_meses = {
                "Enero" : 1,
                "Febrero" : 2,
                "Marzo" : 3,
                "Abril" :4,
                "Mayo" :5,
                "Junio":6,
                "Julio":7,
                "Agosto":8,
                "Septiembre":9,
                "Octubre":10,
                "Noviembre":11,
                "Diciembre":12
}


if "/" in fecha:
    lista_fecha = fecha.split("/")
    mes = int(lista_fecha[0])
    dia = int(lista_fecha[1])
    anio = int(lista_fecha[2])
else:
    lista_fecha = fecha.split(", ")
    anio = int(lista_fecha[1])
    lista_fecha_2 = lista_fecha[0].split(" ")
    dia = int(lista_fecha_2[1])
    mes = int(lista_meses[lista_fecha_2[0]])



print(f"{anio}-{mes:02}-{dia:02}")
    