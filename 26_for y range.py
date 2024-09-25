# Usamos un bucle for para iterar a través de un rango de números
for numero in range(1, 11):  # Del 1 al 10 (11 no incluido)
    # Verificamos si el número es par
    if numero % 2 == 0:
        # Si el número es par, imprimimos el mensaje correspondiente
        print(f"{numero} es par.")
    else:
        # Si el número no es par (es impar), imprimimos el mensaje correspondiente
        print(f"{numero} es impar.")
