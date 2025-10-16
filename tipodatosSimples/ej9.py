capital=float(input("¿Cuánto dinero quieres invertir?"))
interes=float(input("¿Cuál es el interés? (En porcentaje)"))
tiempo=float(input("¿Durante cuánto tiempo? (En años)"))

a=(capital * (1 + interes / 100) ** tiempo)

print("Vas a ganar",round(a,2))