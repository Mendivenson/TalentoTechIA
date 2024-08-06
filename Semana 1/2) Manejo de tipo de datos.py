# ==========================================================
# Manejo de tipo de datos con python
# Autor: Michel Mendivenson Barragán Zabala
# IA (Nivel explorador, TalentoTech)
# ==========================================================

# Identifica el tipo de dato (int, float, string o list) de los siguientes valores literales:
# * "Hola Mundo"
# * [1, 10, 100]
# *  -25
# * 1.167
# * ["Hola", "Mundo"]
# * ' '
# * True
# * A={Uno:"uno", Dos:"dos"}

lista = ['Hola Mundo', [1,10,100], -25, 1.167, ['Hola', 'Mundo'], ' ', True, {'Uno': 'uno', 'Dos':'dos'}]
for i in lista:
    print(i)
    print(type(i))
