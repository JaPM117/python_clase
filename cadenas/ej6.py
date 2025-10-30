frase=input("Introduce una frase")
vocal=str(input("Introduce una vocal que aparezca en la frase"))

vocal_lower=vocal.lower()

frase_modificada=frase.replace(str(vocal_lower),str(vocal.upper()))

print(frase_modificada)