# ==========================================================
# Manejo de IF
# Autor: Michel Mendivenson Barragán Zabala
# IA (Nivel explorador, TalentoTech)
# ==========================================================

# Realizar un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
# - Mostrar una suma de los dos números
# - Mostrar una resta de los dos números (el primero menos el segundo)
# - Mostrar una multiplicación de los dos números
# En caso de no introducir una opción válida, el programa informará que la opción no es correcta.


def verify(caption = 'Introduzca el valor:', tipo = str):
    flag = True
    while flag:
        valor = input(caption)
        try:
            valor = tipo(valor)
            flag = False
        except ValueError:
            print('\n', 20 * '=', '\t Valor incorrecto se espera que ingrese un valor de tipo', tipo, '. Intente de nuevo \t', 20 * '=', '\n')
    return valor

num1 = verify('Introduzca el valor del número 1: ', float)
num2 = verify('Introduzca el valor del número 2: ', float)

print("Este programa cuenta con 3 opciones:\n \
\t 1) Sumar los números\n \
\t 2) Restar el número 1 menos e número 2\n \
\t 3) Multiplicar los dos números\n \
Si desea salir, simplemente ingrese 0.")


seleccion = 5
opciones = [0,1,2,3]

while seleccion not in opciones:
    seleccion = verify('\n ====> Seleccione la opción de su intéres: ', int)

if seleccion == 3:
    print(f'\n\n{40 * '='} \n La multiplicación de los dos números es: {num1 * num2}\n{40 * '='}')
if seleccion == 2:
    print(f'\n\n {40 * '='} \n La resta de los dos números es: {num1 - num2}\n{40*'='}')
if seleccion == 1:
    print(f'\n\n {40 * '='} \n La suma de los dos números es: {num1 + num2}\n{40*'='}')
if seleccion == 0:
    print(f'\n\n {20 * '='} Buen día {20*'='}')
