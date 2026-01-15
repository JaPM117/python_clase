fruta=input("¿Qué fruta quieres?")
kilos=int(input("¿Cuántos kilos quieres?"))

precios={
    'Plátano':1.35,
    'Manzana':0.80,
    'Pera':0.85,
    'Naranja':0.70,
}

total=precios[fruta]*kilos

if fruta in precios:
    print("Debes pagar",total,"euros")

else:
    print("Ese producto no está en nuestro catálogo")