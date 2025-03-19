import math

# Función para calcular el perímetro (circunferencia) de un círculo
def perimetro_circulo(radio):
    return 2 * math.pi * radio

# Solicitar al usuario que ingrese el valor del radio
radio = float(input("Ingresa el valor del radio del círculo: "))

# Calcular el perímetro y mostrar el resultado
perimetro = perimetro_circulo(radio)
print(f"El perímetro del círculo es: {perimetro}")
