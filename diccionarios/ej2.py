nombre=input("Escribe tu nombre: ")
edad=int(input("Escribe tu edad: "))
dir=input("Escribe tu dirección: ")
tel=int(input("Escribe tu teléfono: "))

diccionario={
    'Nombre':nombre,
    'Edad':edad, 
    'Dirección':dir, 
    'Teléfono':tel
    }

print(diccionario["Nombre"],"tiene",diccionario['Edad'],"años, vive en",diccionario['Dirección'],"y su número de teléfono es",diccionario["Teléfono"])