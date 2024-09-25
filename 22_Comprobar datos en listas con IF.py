
edades_permitidas = [18, 21, 25, 30, 35]

# Solicitamos al usuario que ingrese su edad
edad = int(input("Ingresa tu edad: "))

# Condicional que verifica si la edad está en la lista
if edad in edades_permitidas:
    print(f"Tu edad {edad} está en la lista permitida.")
else:
    print(f"Tu edad {edad} no está en la lista permitida.")
