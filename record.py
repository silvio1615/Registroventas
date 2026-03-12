

def register_product():
    # Función para registrar un producto
    print("Bienvenido al sistema de registro de ventas")
    print("Ingrese los datos del producto que desea registrar")
    product = (input("Ingrese el nombre del producto: "))
    quantity = int(input("Ingrese la cantidad del producto: "))
    price = float(input("Ingrese el precio del producto: "))
#    
    total = price * quantity
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
        print("thank you for using the sales registration system.")
        for sale in sales:
            print(f"product:{sale['product']}")
            print(f"price:{sale['price']}")
            print(f"quantity:{sale['quantity']}")
            print(f"total:{sale['total']}")


def sales_summary(sales):
    # sum all totals from every sale and print the total sales
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
