
def registro_producto():
    print("Bienvenido al sistema de registro de ventas")
    print("Ingrese los datos del producto que desea registrar")
    producto = (input("Ingrese el nombre del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    total = precio*cantidad
    venta = {
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio,
        "total": total
    }
    return venta


def resumen_ventas(ventas):
    if not ventas:
        print("no hay ventas registradas.")
    else:
        for venta in ventas:
            print(f"producto:{venta['producto']}")
            print(f"precio:{venta['precio']}")
            print(f"cantidad:{venta['cantidad']}")
            print(f"total:{venta['total']}")


def mostrar_venta(ventas):
    total_ventas = sum(venta["total"]for venta in ventas)
    print(f"total de ventas:{total_ventas}")
