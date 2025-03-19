# Función para calcular el perímetro de un cuadrado
def perimetro_cuadrado(lado):
    return 4 * lado

# Solicitar al usuario que ingrese el valor del lado
lado = float(input("Ingresa el valor del lado del cuadrado: "))

# Calcular el perímetro y mostrar el resultado
perimetro = perimetro_cuadrado(lado)
print(f"El perímetro del cuadrado es: {perimetro}")
