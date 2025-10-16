print("Vamos a calcular tu IMC")

peso=input("Introduce tu peso" )
altura=input("Introduce tu altura")
imc=float(peso)/float(altura)**2
print("tu IMC es " ,round(imc,2))