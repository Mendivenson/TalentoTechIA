# ==========================================================
# Manejo de WHILE en python
# Autor: Michel Mendivenson Barragán Zabala
# IA (Nivel explorador, TalentoTech)
# ==========================================================



# Realiza un programa que:
# - Pida al usuario un número entero del 0 al 9, y que mientras el número 
#   no sea correcto se repita el proceso.
# - Debe comprobar si el número se encuentra en la lista de números y notificarlo.
# Sugerencia: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)

lista = [1,3,6,9,0]

flag = True
while flag:
    try:
        numero = int(input('\nIngrese un número del 0 al 9 para verificar si está en la lista: '))
        if numero < 0 or numero > 9:
            raise ValueError()
        flag = False
    except ValueError: 
        print('\n\n',20 * '=', 'Intente de nuevo. El número ingresado no es válido (Invalid type or not between 0 and 9)', 20 * '=', '\n')

if numero in lista:
    print(f'\nEl número ingresado por el usuario ({numero}) está en la lista\n')
else:
    print(f'\nEl número ingresado por el usuario ({numero}) no está en la lista\n')
