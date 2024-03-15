# Solicitar al usuario el monto total de la compra
monto_compra = float(input("Ingrese el monto total de la compra: "))

def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (monto_total * porcentaje_descuento) / 100
    total_a_pagar = monto_total - descuento
    return total_a_pagar


# Ejemplo de uso
descuento = 10
total_a_pagar = calcular_descuento(monto_compra, descuento)
print(f"El total a pagar con un {descuento}% de descuento es: {total_a_pagar}")