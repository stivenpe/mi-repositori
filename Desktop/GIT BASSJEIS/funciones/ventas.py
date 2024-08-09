import json
from datetime import datetime

def registrar_venta(fecha, cliente, empleado, productos):


    venta = {
        "fecha": fecha,
        "cliente": {
            "nombre": cliente["nombre"],
            "direccion": cliente["direccion"]
        },
        "empleado": {
            "nombre": empleado["nombre"],
            "cargo": empleado["cargo"]
        },
        "productos": [
            {
                "nombre": producto["nombre"],
                "cantidad": producto["cantidad"],
                "precio": producto["precio"]
            }
            for producto in productos
        ]
    }

    
    try:
        with open('date.json', 'r') as file:
            datos_ventas = json.load(file)
    except FileNotFoundError:
        datos_ventas = []

    
    datos_ventas.append(venta)

    
    with open('data.json', 'w') as file:
        json.dump(datos_ventas, file, indent=4)

fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cliente = {
    "nombre": "Juan Pérez",
    "direccion": "Calle Falsa 123"
}
empleado = {
    "nombre": "Ana Gómez",
    "cargo": "Vendedora"
}
productos = [
    {"nombre": "Producto A", "cantidad": 2, "precio": 10.50},
    {"nombre": "Producto B", "cantidad": 1, "precio": 25.00}
]

registrar_venta(fecha, cliente, empleado, productos)


if __name__ == "__main__":
     registrar_venta()