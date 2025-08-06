#programa compra de boletos de cine
edad = int(input("Ingresa tu edad del cliente: "))

if edad < 4:
    print("La entrada es gratis")
elif edad > 4 and edad<=12:
    print("Boleto infantil, paga $40")
elif edad > 12 and edad <=59:
    print("pago general de $70")
else:
    print("pago de una persona mayor, de $35")

