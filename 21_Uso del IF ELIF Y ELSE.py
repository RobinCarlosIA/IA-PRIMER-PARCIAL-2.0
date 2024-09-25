# Solicitamos la edad al usuario
edad = int(input("Ingresa tu edad: "))

# Verificamos si la persona es mayor de 18 años
if edad >= 18:
    print("Eres mayor de edad.")  # Se ejecuta si la edad es 18 o más
# Verificamos si la persona es adolescente (13 a 17 años)
elif edad >= 13:
    print("Eres adolescente.")  # Se ejecuta si la edad está entre 13 y 17
# Si no cumple ninguna de las anteriores, es un niño (menor de 13 años)
else:
    print("Eres un niño.")  # Se ejecuta si la edad es menor a 13
