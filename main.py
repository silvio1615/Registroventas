from registro import registro_producto, resumen_ventas, mostrar_venta
ventas = []
continuar = "s"
while continuar.lower == "s":
    venta = registro_producto()
    ventas.append(venta)
    print("venta registrada exitosamente")
    continuar = input("desea registrar otro producto? (s/n)")
else:
    mostrar_venta(ventas)
    resumen_ventas(ventas)
