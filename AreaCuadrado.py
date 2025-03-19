# Función para calcular el área de un cuadrado
def area_cuadrado(lado):
    return lado ** 2

# Solicitar al usuario que ingrese el valor del lado
lado = float(input("Ingresa el valor del lado del cuadrado: "))

# Calcular el área y mostrar el resultado
area = area_cuadrado(lado)
print(f"El área del cuadrado es: {area}")
