#import the functions from the record.py file to use them in the main.py file
from record import register_product,show_sales,sales_summary
sales = []
continuar = "s"
#continuar = input("do you want to register a product? (s/n)")
# use while for to keep asking the user if they want to register a product until they say no, then show the sales summary
while continuar.lower() == "s":
    # call the function to register a product and store the returned dictionary in a variable, then append it to the sales list and ask the user if they want to register another product
    regist = register_product()
    # append the sale to the sales list
    sales.append(regist)
    print("sale registered successfully")
    continuar = input("do you want to register another sales? (s/n)")
# call the functions to show the sales and the sales summary and parameterize them with the sales list where the sales are stored 
show_sales(sales)   
sales_summary(sales)
print("thank you for using the sales registration system")




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
