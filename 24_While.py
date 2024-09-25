numero = 0

# Usamos un bucle while para seguir pidiendo un número
while numero >= 0:
    numero = int(input("Ingresa un número (negativo para salir): "))
    if numero >= 0:
        print(f"Has ingresado: {numero}")

print("Has ingresado un número negativo. Saliendo...")