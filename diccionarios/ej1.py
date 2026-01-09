nombre=input("Escribe una divisa: ")

diccionario= {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

if nombre in diccionario:
    print (diccionario[nombre])

else:
    print("Esa divisa no está en el diccionario")