import math

numero_1 = float(input("Introduce el primer número: "))
numero_2 = float(input("Introduce el segundo número: "))
numero_3 = float(input("Introduce el tercer número: "))


if numero_2 < 0:
    suma = numero_1 + numero_3
    raiz_cuadrada = math.sqrt(suma)
    print("La raíz cuadrada de la suma de los números restantes es:", raiz_cuadrada)
else:
    print("Error: El segundo número no es negativo.")
    
