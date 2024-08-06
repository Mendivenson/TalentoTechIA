# ==========================================================
# Manejo de string con python
# Autor: Michel Mendivenson Barragán Zabala
# IA (Nivel explorador, TalentoTech)
# ==========================================================

# Escriba una función que indique si una frase es palíndroma. 
# Una frase es palíndroma si se lee igual de derecha a izquierda 
# que de izquierda a derecha, pero obviando los espacios en blanco
# y los signos de puntuación. Por ejemplo, las cadenas: 
# "Sé verla al revés", "Anita lava la tina", "luz azul" 
# contienen frases palíndromas.

def pal(palabra = '12321'):
    "Esta función define si un string es o no palindromo"
    x = palabra.replace(' ', '').lower().translate(str.maketrans('áéíóú', 'aeiou'))
    y = list(x)
    y.reverse()
    x = list(x)
    if (x == y):
        print(f'La cadena de texto *{palabra}* es un palíndromo')
    else:
        print(f'La cadena de texto *{palabra}* NO es un palíndromo')


palabra = input('Inserte una cadena de carácteres: ')
pal(palabra)
