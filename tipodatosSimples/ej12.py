ventas_ant=int(input("¿Cuántas barras, que no sean del día, se van a vender? "))

barra_día=3.49
descuento=float(barra_día*0.06)
barra_ant=barra_día-descuento

print("El precio de una barra del día es de", barra_día)
print("Las barras que no son frescas tienen un descuento de", descuento)
print(f"El coste total de las barras de otros días vendidas es de {(ventas_ant*barra_ant):.2f}")