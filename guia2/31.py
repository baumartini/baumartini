import math

numero_1 = float(input("Introduce el primer número: "))
numero_2 = float(input("Introduce el segundo número: "))
numero_3 = float(input("Introduce el tercer número: "))

if numero_1 == 1:
    resultado = numero_2 + numero_3
    print("Resultado (suma):", resultado)
elif numero_1 == 2:
    resultado = numero_2 * numero_3
    print("Resultado (multiplicación):", resultado)
elif numero_1 == 3:
    if numero_3 != 0:  
        resultado = numero_2 / numero_3
        print("Resultado (división):", resultado)
    else:
        print("Error: División por cero.")
elif numero_1 == 4:
    resultado = math.sqrt(numero_2**2 + numero_3**2)
    print("Resultado (raíz cuadrada de la suma de los cuadrados):", resultado)
else:
    print("Error: Valor no válido.")
    
