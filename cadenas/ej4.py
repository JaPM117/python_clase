tlf=input("Introduce tu número de tlf con este formato -> +XX-XXXXXXXXX-XX")

partes = tlf.split('-')

print("Tu teléfono sin prefijo ni exntensión es el siguiente:",partes[1])