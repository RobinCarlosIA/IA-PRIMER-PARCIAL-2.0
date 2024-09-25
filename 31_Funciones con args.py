# Definimos una función que suma un número variable de argumentos
def sumar(*numeros):
    total = 0  # Inicializamos la variable total en 0
    for numero in numeros:  # Iteramos sobre cada número pasado como argumento
        total += numero  # Sumamos cada número al total
    return total  # Devolvemos la suma total

# Llamamos a la función con varios argumentos
resultado = sumar(10, 22, 43, 54, 85)  # Pasamos múltiples argumentos a la función
print(f"La suma es: {resultado}")  # Imprimimos el resultado de la suma
