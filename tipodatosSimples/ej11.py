dinero_ini=float(input("Introduce la cantidad de dinero depositada: "))

interes=0.04

año1 = dinero_ini*(1+interes)
año2 = año1*(1+interes)
año3 = año2*(1+interes)

print(f"Tras el primer año: {año1:.2f} €")
print(f"Tras el segundo año: {año2:.2f} €")
print(f"Tras el tercer año: {año3:.2f} €")