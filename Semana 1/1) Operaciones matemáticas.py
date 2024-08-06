# ==========================================================
# Operaciones con matemáticas con python
# Autor: Michel Mendivenson Barragán Zabala
# IA (Nivel explorador, TalentoTech)
# ==========================================================

# Realiza un programa que cumpla con el siguiente algoritmo, utilizando siempre que sea posible, operadores en asignación:
# - Guarda en una variable numero_magico el valor 12345679 (sin el 8)
# - Asignar a otra variable numero_usuario. Hay que especificar que sea entre 1 y 9 (asegúrate que es un número)
# - Multiplica el numero_usuario por 9 en sí mismo
# - Multiplica el numero_magico por el numero_usuario en sí mismo
# - Finalmente muestra el valor final del numero_magico por pantall

numero_magico = 12345679
numero_usuario = int(input('Ingresa un número entero entre 1 y 9 (inclusive): '))
if (numero_usuario < 1 or numero_usuario > 9):
    print('Se debe ingresar un número válido')
else: 
    numero_usuario = numero_usuario * 9
    numero_usuario = numero_usuario * numero_magico
    print(numero_usuario)
