precioCompra= 97.00
precioVenta= 113.00

pesos= float (input("Ingrese su saldo en pesos: "))
dolares = float (input("Ingrese saldo en dolares: "))

pesosADolares = pesos/precioVenta
dolaresAPesos = dolares* precioCompra

saldoEnPesos = pesos + dolaresAPesos
saldoEnDolares =dolares + pesosADolares

print("Su saldo total en pesos es:", saldoEnPesos)
print("Su saldo total en dolares es:", saldoEnDolares)

