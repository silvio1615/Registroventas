from record import register_product,show_sales,sales_summary
sales = []
continuar = "s"
continuar = input("do you want to register a product? (s/n)")
while continuar.lower() == "s":
    sale = register_product()
    sales.append(sale)
    print("sale registered successfully")
    continuar = input("do you want to register another sales? (s/n)")

sales_summary(sales)
show_sales(sales)





# from registro import registro_producto, resumen_ventas, mostrar_venta
# ventas = []
# continuar = "s"
# while continuar.lower == "s":
#     venta = registro_producto()
#     ventas.append(venta)
#     print("venta registrada exitosamente")
#     continuar = input("desea registrar otro producto? (s/n)")
# else:
#     mostrar_venta(ventas)
#     resumen_ventas(ventas)
