personas = {
    "Juan": {"edad": 30, "ciudad": "Madrid"},
    "Ana": {"edad": 25, "ciudad": "Barcelona"},
    "Luis": {"edad": 28, "ciudad": "Valencia"}
}

# Imprimimos la información de cada persona
for nombre, info in personas.items():  # Iteramos sobre cada persona y su información
    print(f"Nombre: {nombre}")  # Imprimimos el nombre
    print(f"  Edad: {info['edad']}")  # Accedemos e imprimimos la edad
    print(f"  Ciudad: {info['ciudad']}")  # Accedemos e imprimimos la ciudad
    print()  # Línea en blanco para mejor legibilidad
