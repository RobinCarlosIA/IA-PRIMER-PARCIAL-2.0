frutas = {
    "manzana": {"color": "rojo", "precio": 1.5},  # Información sobre la manzana
    "plátano": {"color": "amarillo", "precio": 1.2},  # Información sobre el plátano
    "naranja": {"color": "naranja", "precio": 1.0}  # Información sobre la naranja
}

print("Frutas originales:")
for fruta, info in frutas.items():  # Iteramos sobre cada fruta y su información
    print(f"{fruta}: {info}")  # Imprimimos el nombre y la información de cada fruta

# Eliminamos la fruta "plátano" del diccionario
del frutas["plátano"]  # Utilizamos 'del' para eliminar la entrada del plátano

# Imprimimos el diccionario después de la eliminación
print("\nFrutas después de eliminar el plátano:")
for fruta, info in frutas.items():  # Iteramos sobre el diccionario modificado
    print(f"{fruta}: {info}")  # Imprimimos el nombre y la información de cada fruta restante
