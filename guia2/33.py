numero=int(input("Introduce un número entre 1 y 7: "))

dias_semana = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}
if 1 <= numero <= 7:
    print(f"El día de la semana correspondiente es: {dias_semana[numero]}")
else:
    print("El número no está en el rango de 1 a 7.")
    