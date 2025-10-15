import string
import secrets

def contiene_mayusculas(password)->bool:
    """Verifica si un password tiene mayúsculas"""
for letra in password:
    if letra.isupper():
        return True
    return False 
def contiene_simbolos(password) -> bool:
    """Verifica si un password tiene simbolos"""
    for letra in password:
        if letra in string.punctuation:
            return True
        return False 
    
def generar_password(longitud, tiene_simbolos, tiene_mayusculas) -> str:
"""
Genera un password basado en las especificaciones del usuario

:param longitud: La longitud del password
:param tiene_simbolos: el password debe incluir simbolos
:param tiene_mayusculas: el password debe incluir mayusculas
:return: str
"""
combinacion = string.ascii_lowercase + string.digits


if tiene_simbolos:
    combinacion += string.punctuation

if tiene_mayusculas:
    combinacion += string.ascii_uppercase

longitud_combinacion = len(combinacion)

nuevo_password = ''

for _ in range(longitud):
    nuevo_password += combinacion[secrets.randbelow(longitud_combinacion)]
    return nuevo_password
if __name__ == '__manin__':
    for i in range(1, 6):
   
     especificaciones = (f'Mayúsculas: {contiene_mayusculas(nuevo_pass)}, '
                        f'Simbolos: {contiene_simbolos(nuevo_pass)}')

print(f'{i} -> {nuevo_pass} ({especificaciones})')
