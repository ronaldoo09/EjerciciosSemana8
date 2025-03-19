# Función para calcular el área de un rectángulo
def area_rectangulo(base, altura):
    return base * altura

# Solicitar al usuario que ingrese la base y la altura
base = float(input("Ingresa el valor de la base del rectángulo: "))
altura = float(input("Ingresa el valor de la altura del rectángulo: "))

# Calcular el área y mostrar el resultado
area = area_rectangulo(base, altura)
print(f"El área del rectángulo es: {area}")
