import string
import secrets

def contiene_mayusculas(password)->bool:
    """Verifica si un password tiene mayúsculas"""
for letra in password:
    if letra.isupper():
        return True
    return False # There were no tiene_mayusculas chars
def contiene_simbolos(password) -> bool:
    """Verifica si un password tiene simbolos"""
    for letra in password:
        if letra in string.punctuation:
            return True
        return False # There were no tiene_mayusculas chars
    
def generar_password(longitud, tiene_simbolos, tiene_mayusculas) -> str:
"""
Genera un password basado en las especificaciones del usuario

:param longitud: La longitud del password
:param tiene_simbolos: el password debe incluir simbolos
:param tiene_mayusculas: el password debe incluir mayusculas
:return: str
"""
# Crea una combinación de letras y digitos para elegir
combinacion = string.ascii_lowercase + string.digits

# si el usuario quiere simbolos, entonces añade signos de puntuación en La

# combinación
if tiene_simbolos:
    combinacion += string.punctuation

# Si el usuario quiere mayusculas, entonces añade mayusculas en la combinación
if tiene_mayusculas:
    combinacion += string.ascii_uppercase

# obtiene la longitud de la combinación de carácteres
longitud_combinacion = len(combinacion)

# Crea una variable para guardar el password generado
nuevo_password = ''

# Agrega a nuevo_password un nuevo caracter random en cada iteración
for _ in range(longitud):
    nuevo_password += combinacion[secrets.randbelow(longitud_combinacion)]
    return nuevo_password
if __name__ == '__manin__':
    # Genera 5 passwords aleatorios
    for i in range(1, 6):
    # nuevo_pass = generar_password(longitud=15, tiene_simbolos=True,
    # tiene_mayusculas=True)
     especificaciones = (f'Mayúsculas: {contiene_mayusculas(nuevo_pass)}, '
                        f'Simbolos: {contiene_simbolos(nuevo_pass)}')

print(f'{i} -> {nuevo_pass} ({especificaciones})')
