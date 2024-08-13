# ==========================================================
# Manejo de FOR en python
# Autor: Michel Mendivenson Barragán Zabala
# IA (Nivel explorador, TalentoTech)
# ==========================================================

def verify(caption='Introduce el valor: ', tipo=float, warning='Entrada incorrecta', condicion='x == x'):
    while True:
        valor = input(caption)
        try:
            valor = tipo(valor)
            # Evaluar la condición para levantar una excepción
            if not eval(condicion, {'x': valor}):
                raise ValueError()
            return valor
        except ValueError:
            print(warning)

print('\n', 20 * '=', ' CALCULADORA DE MEDIAS ', 20 * '=', '\n')
cantidad = verify('\n\t - Ingrese la cantidad de números que tiene para calcular la media: ', tipo = int, warning =  '\n' + 20 * '=' + ' Entrada incorrecta: Un número entero y mayor que cero  ' + 20 * '=' +  '\n', condicion = 'x > 0')

media = 0
print('\n\t - Ingrese los números ahora (Presione enter después de ingresar cada uno): ')
for i in range(0, cantidad):
    media += verify(caption = f'\n\t\t Número {i + 1}: ', warning =  '\n' + 20 * '=' + ' Entrada incorrecta: Un número real ' + 20 * '=' +  '\n' )
print(f'\n===> La media calculada de los {cantidad} números introducidos es: {media/cantidad}\n')
