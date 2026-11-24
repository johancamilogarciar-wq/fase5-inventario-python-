def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


inventario = [
    ["1", "Teclado", 4, 10],
    ["2", "Mouse", 15, 10],
    ["3", "Monitor", 2, 5],
    ["4", "Cable HDMI", 8, 8],
    ["5", "Audifonos", 1, 6],
]

print("Artículos a pedir:")
for codigo, nombre, stock_actual, stock_minimo in inventario:
    cantidad_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
    print(f"{nombre}: {cantidad_pedir}")