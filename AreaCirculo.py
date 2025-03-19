import math

# Función para calcular el área de un círculo
def area_circulo(radio):
    return math.pi * radio ** 2

# Solicitar al usuario que ingrese el valor del radio
radio = float(input("Ingresa el valor del radio del círculo: "))

# Calcular el área y mostrar el resultado
area = area_circulo(radio)
print(f"El área del círculo es: {area}")
