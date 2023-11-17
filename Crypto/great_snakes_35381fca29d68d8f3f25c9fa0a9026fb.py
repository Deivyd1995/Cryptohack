#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")


ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]


#  Ese fragmento de código (chr(o ^ 0x32) for o in ords) utiliza una expresión
#  generadora para aplicar la operación XOR a cada elemento o en la lista ords
#  con el valor hexadecimal 0x32. Luego, utiliza la función chr() para convertir
#  cada resultado de la operación XOR de nuevo en un carácter.

# Entonces, el primer número se transforma en 99.
#  Este proceso se repite para cada número en la lista.

print("Here is your first flag:")
print("".join(chr(o ^ 0x32) for o in ords))

# In Python, the chr() function can be used to convert an ASCII ordinal number to a character (the ord() function does the opposite).

listaNumeros = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
print("Here is your second flag:")
print("".join(chr(o) for o in listaNumeros))

