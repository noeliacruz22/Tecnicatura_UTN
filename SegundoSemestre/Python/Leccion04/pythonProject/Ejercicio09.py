#Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
#Hacer un programa donde el usuario ingrese una frase, se le devolvera la misma
#frase pero sin espacios en blanco, y ademas un contador de cuantos caracteres tiene
#la frase sin contar espacios en blanco
#Ejemplo: frase = vivir por siempre en paz
#         frase final = vivirporsiempreenpaz
#         n° de caracteres = 21

frase1 = input('Ingrese una frase: ')
print(f'\nFrase ingresada: {frase1}')
frase2 = ' '
for i in frase1:
    if i != ' ':
        frase2 += i
frase1 = frase2
print(f'\nFrase final: {frase1}')
print(f'Total de caracteres: {len(frase1)}')