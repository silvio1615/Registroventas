def register_product():
    # ask the user for the product name, quantity and price, calculate the total and return a dictionary with the sale details
    print("welcome to the sales registration system")
    print("please enter the product details")
    
    product = (input("enter the product name: "))
    quantity = int(input("enter the product quantity: "))
    price = float(input("enter the product price: "))
    total = price * quantity
    # create a dictionary with the sale details and return it
    sale = {
        "product": product,
        "quantity": quantity,
        "price": price,
        "total": total
    }
    return sale


def show_sales(sales):
    # if the list is empty,notify the user that no sales have been recorded, otherwise print the details of each sale
    if not sales:
        print("no sales recorded.")
    else:
        print("sales registered:")
        for sale in sales:
            print(f"product:{sale['product']}")
            print(f"price:{sale['price']}")
            print(f"quantity:{sale['quantity']}")
            print(f"total:{sale['total']}")
            
# use sales summary  parameterized with the sales list to sum all totals from every sale and print the total sales
def sales_summary(sales):
    total_sales = sum(sale["total"] for sale in sales)
    print(f"total of sales: {total_sales}")


# def registro_producto():
#     print("Bienvenido al sistema de registro de ventas")
#     print("Ingrese los datos del producto que desea registrar")
#     producto = (input("Ingrese el nombre del producto: "))
#     cantidad = int(input("Ingrese la cantidad del producto: "))
#     precio = float(input("Ingrese el precio del producto: "))
#     total = precio*cantidad
#     venta = {
#         "producto": producto,
#         "cantidad": cantidad,
#         "precio": precio,
#         "total": total
#     }
#     return venta


# def resumen_ventas(ventas):
#     if not ventas:
#         print("no hay ventas registradas.")
#     else:
#         for venta in ventas:
#             print(f"producto:{venta['producto']}")
#             print(f"precio:{venta['precio']}")
#             print(f"cantidad:{venta['cantidad']}")
#             print(f"total:{venta['total']}")


# def mostrar_venta(ventas):
#     total_ventas = sum(venta["total"]for venta in ventas)
#     print(f"total de ventas:{total_ventas}")
