prod=str(input("Introduce el nombre de un producto. "))
prec=float(input("Introduce el precio del producto. "))
num=int(input("Introduce el número de unidades. "))

total= prec * num

print(f"PRECIO UNITARIO: {prec:.2f} €")
print(f"NÚMERO DE UNIDADES:", num)
print(f"COSTE TOTAL: {total:.2f} €"