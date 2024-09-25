
numero = 0

# Usamos un bucle while que se ejecutará indefinidamente
while True:
    # Pedimos al usuario que ingrese un número
    numero = int(input("Ingresa un número (negativo para salir): "))
    
    # Verificamos si el número es negativo
    if numero < 0:
        print("Has ingresado un número negativo. Saliendo...")
        break  # Salimos del bucle si el número es negativo
    
    # Si el número no es negativo, mostramos el número ingresado
    print(f"Has ingresado: {numero}")
