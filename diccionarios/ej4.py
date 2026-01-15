fecha=(input("¿Qué fecha es?(dd/mm/aaaa)"))

date=fecha.split("/")

meses={
    '01':'Enero',
    '02':'Febrero',
    '03':'Marzo',
    '04':'Abril',
    '05':'Mayo',
    '06':'Junio',
    '07':'Julio',
    '08':'Agosto',
    '09':'Septiembre',
    '10':'Octubre',
    '11':'Noviembre',
    '12':'Diciembre',
}

print(date[0],"de",meses[date[1]],"del",date[2])