# Función para calcular el perímetro de un rectángulo
def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

# Solicitar al usuario que ingrese la base y la altura
base = float(input("Ingresa el valor de la base del rectángulo: "))
altura = float(input("Ingresa el valor de la altura del rectángulo: "))

# Calcular el perímetro y mostrar el resultado
perimetro = perimetro_rectangulo(base, altura)
print(f"El perímetro del rectángulo es: {perimetro}")
