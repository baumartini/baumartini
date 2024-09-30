numero = int(input("Introduce un número entero positivo menor que 100: "))

if numero < 1 or numero >= 100:
    print("Error: El número debe ser un entero positivo menor que 100.")
else:
    
    if numero == 2 or numero == 3 or numero == 5 or numero == 7:
        print(f"{numero} es un número primo.")
    elif numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
        print(f"{numero} no es un número primo.")
    else:
        print(f"{numero} es un número primo.")
        
