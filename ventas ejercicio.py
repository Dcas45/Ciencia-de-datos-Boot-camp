# 1. lista de diccionarios con ventas
ventas = [
    {"fecha": "2024-01-01", "producto": "Manzana", "cantidad": 10, "precio": 0.5},
    {"fecha": "2024-01-01", "producto": "Banana", "cantidad": 5, "precio": 0.3},
    {"fecha": "2024-01-02", "producto": "Manzana", "cantidad": 7, "precio": 0.5},
    {"fecha": "2024-01-02", "producto": "Naranja", "cantidad": 8, "precio": 0.6},
    {"fecha": "2024-01-03", "producto": "Banana", "cantidad": 10, "precio": 0.35},
    {"fecha": "2024-01-03", "producto": "Naranja", "cantidad": 6, "precio": 0.6},
]

# 2. Ingresos Totales
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

print("Ingresos Totales:", ingresos_totales)

# 3.  Producto Más Vendido
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    if producto not in ventas_por_producto:
        ventas_por_producto[producto] = 0
    ventas_por_producto[producto] += cantidad

# Producto con mayor cantidad total vendida
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

print("Producto más vendido:", producto_mas_vendido)
print("Cantidad total vendida:", cantidad_mas_vendida)

# 4. Promedio de Precio por Producto
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]

    if producto not in precios_por_producto:
        precios_por_producto[producto] = (0, 0)  # (suma_precios, cantidad_total)

    suma_precios, cant_total = precios_por_producto[producto]
    suma_precios += precio * cantidad
    cant_total += cantidad
    precios_por_producto[producto] = (suma_precios, cant_total)

# Calcular precio promedio por producto
precio_promedio_por_producto = {}
for producto, (suma_precios, cant_total) in precios_por_producto.items():
    precio_promedio_por_producto[producto] = suma_precios / cant_total

print("Precio promedio por producto:")
for producto, precio_promedio in precio_promedio_por_producto.items():
    print(f"  {producto}: {precio_promedio:.2f}")

# 5. Ventas por Día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    if fecha not in ingresos_por_dia:
        ingresos_por_dia[fecha] = 0
    ingresos_por_dia[fecha] += ingreso

print("Ingresos por día:")
for fecha, ingreso in ingresos_por_dia.items():
    print(f"  {fecha}: {ingreso:.2f}")

# 6. Representación de Datos - Resumen de Ventas
resumen_ventas = {}
for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]
    ingresos_totales_producto = precio_promedio_por_producto[producto] * cantidad_total
    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": ingresos_totales_producto,
        "precio_promedio": precio_promedio_por_producto[producto]
    }

print("Resumen de ventas por producto:")
for producto, resumen in resumen_ventas.items():
    print(f"{producto}: {resumen}")
