#!/usr/bin/env python3

import sys
import base64
import Crypto.Util.number as cripto
import funcionesUtiles
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

# ASCII and XOR
print("----------------------------------------------------------------------------")

#  Ese fragmento de código (chr(o ^ 0x32) for o in ords) utiliza una expresión
#  generadora para aplicar la operación XOR a cada elemento o en la lista ords
#  con el valor hexadecimal 0x32.
# 81 (en binario) = 1010001
# 0x32 (en binario) = 0110010
# Resultado de XOR: 1100011 (en decimal es 99) Luego, utiliza la función chr() para convertir
#  cada resultado de la operación XOR de nuevo en un carácter.

# Entonces, el primer número se transforma en 99.
#  Este proceso se repite para cada número en la lista.

# In Python, the chr() function can be used to convert an ASCII ordinal number to a character
#  (the ord() function does the opposite).



ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
print("Here is your first flag:")
print("".join(chr(o ^ 0x32) for o in ords))
print("----------------------------------------------------------------------------")

# Usando la siguientes matrizes de enteros,
# convierta los números a sus caracteres ASCII correspondientes para obtener una bandera.
listaNumeros = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
print("Here is your second flag:")
print("".join(chr(o) for o in listaNumeros))
print("----------------------------------------------------------------------------")
# -------------      ----------------------    -------------------      -------------------   --

# Cuando ciframos algo, el texto cifrado resultante normalmente tiene bytes que
# no son caracteres ASCII imprimibles. Si queremos compartir nuestros datos cifrados,
# Es común codificarlo en algo más fácil de usar y portátil en diferentes sistemas.

# El hexadecimal se puede utilizar de tal manera para representar cadenas ASCII.
# Primero, cada letra se convierte en un número ordinal.
# según la tabla ASCII (como en el desafío anterior).
# Luego, los números decimales se convierten a números de base 16, también conocidos como hexadecimales.
# Los números se pueden combinar en una larga cadena hexadecimal.

# En Python, la función bytes.fromhex() se puede utilizar para convertir hexadecimal a bytes.
# Se puede invocar el método de instancia .hex() en cadenas de bytes para obtener la representación hexadecimal.

# A continuación se incluye una bandera codificada como una cadena hexadecimal.
# Decodifica esto nuevamente en bytes para obtener la bandera.

second = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
print("Here is your second flag:")
print(bytes.fromhex(second))
print("----------------------------------------------------------------------------")

# -- --------   ----------     ----------        -------------   ----------       -------------   ----------------

# BASE64
# Base64, nos permite representar datos binarios como una cadena ASCII utilizando un alfabeto de 64 caracteres.
# Un carácter de una cadena Base64 codifica 6 dígitos binarios (bits),
# por lo que 4 caracteres de Base64 codifican tres bytes de 8 bits

# En Python, after importing the base64 module with import base64, you can use
#  the base64.b64encode() function. Remember to decode the hex first as the challenge description states.

# Tome la siguiente cadena hexadecimal, decodifíquela en bytes y luego codifíquela en Base64.
third = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
print("Here is your third flag:")
# Con la siguiente linea transformamos una cadena exadecimal a bytes y la guardamos en una variable:
cosa = bytes.fromhex(third)
print("En bytes")
print(cosa)
# Y luego la codificamos con base64
print("Codificado en Base64")
print(base64.b64encode(cosa)) 
print("----------------------------------------------------------------------------")

# -- --------   ----------     ----------        -------------   ----------       -------------   ----------------
# RSA

# Los criptosistemas como RSA funcionan con números, pero los mensajes se componen de caracteres.
# ¿Cómo deberíamos convertir nuestros mensajes en números para que se puedan aplicar operaciones matemáticas?

# La forma más común es tomar los bytes ordinales del mensaje,
# convertirlos a hexadecimal y concatenar.
# Esto puede interpretarse como un número de base 16/hexadecimal y también representarse en base 10/decimal.

# Para ilustrar:

# mensaje: HOLA
# bytes ascii: [72, 69, 76, 76, 79]
# bytes hexadecimales: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
# base-16: 0x48454c4c4f
# base-10: 310400273487

# La biblioteca PyCryptodome de Python implementa esto con los métodos bytes_to_long()y long_to_bytes().
# Primero tendrás que instalar PyCryptodome e importarlo con from Crypto.Util.number import *.

fourth = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print("Here is your fourth flag:")
fourthBytes = cripto.long_to_bytes(fourth)
print("En bytes")
print(fourthBytes)
print("----------------------------------------------------------------------------")

# -- --------   ----------     ----------        -------------   ----------       -------------   ----------------

# XOR STARTER

# Podemos realizar XOR de números enteros convirtiendo primero el número entero de decimal a binario.
# Podemos XOR cadenas convirtiendo primero cada carácter al número entero que representa el carácter Unicode.

# Dada la cadena label, XOR cada carácter con el número entero 13

fiveth = 'label'
print("Here is your fiveth flag:")
print("crypto{" + funcionesUtiles.xorToCadenaWithNumer(fiveth,13) +"}")
print("----------------------------------------------------------------------------")


# -- --------   ----------     ----------        -------------   ----------       -------------   ----------------

# XOR PROPERTIES


# Conmutativo: A ⊕ B = B ⊕ A
# Asociativo: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
# Identidad: A ⊕ 0 = A
# Autoinverso: A ⊕ A = 0

# Analicemos esto.
#  Conmutativo significa que el orden de las operaciones XOR no es importante.
#  Asociativo significa que se puede realizar una cadena de operaciones sin orden
#  (no tenemos que preocuparnos por los paréntesis).
#  La identidad es 0, por lo que XOR con 0 "no hace nada" 
# y, por último, algo XOR consigo mismo devuelve cero.

# A continuación se muestra una serie de resultados
# en los que se han aplicado XOR a tres claves aleatorias juntas y con la bandera.
# Utilice las propiedades anteriores para deshacer el cifrado en la línea final para obtener la bandera.

# CLAVE1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# CLAVE2 ^ CLAVE1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# CLAVE2 ^ CLAVE3 = c1545 756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1 
# BANDERA ^ CLAVE1 ^ CLAVE3 ^ CLAVE2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

# Extraemos las variables con las que vamos a trabajar
clave1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
clave2Yclave1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
clave2Yclave3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
finalClave = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
# Convertimos cada uno de las variables base a Bytes que es el tipo de dato en el que se encuentra la bandera.
clave1Byts = bytes.fromhex(clave1)
clave2Yclave1Bytes = bytes.fromhex(clave2Yclave1)
clave2Yclave3Bytes = bytes.fromhex(clave2Yclave3)
finalClaveBytes = bytes.fromhex(finalClave)

# Aplicamos la propiedad Asociativo del XOR para obtener el valor de las claves.
#? Si A ^ B = C entonces A ^ C = B es lo mismo que A XOR B = C entonces A XOR C = B.
print("Here is your sixth flag:")
print("Valor de clave 1:")
print(clave1Byts)
print("Valor de clave 2:")
clave2 = funcionesUtiles.xor_bytes(clave1Byts, clave2Yclave1Bytes)
print(clave2)
# Volvemos a aplicar el principio con el resultado anterior y los datos que teniamos de antemano.
print("Valor de clave 3:")
clave3 = funcionesUtiles.xor_bytes(clave2Yclave3Bytes, clave2)
print(clave3)
# Seguimos usando el mismo princio con los valores obtenidos mas los que nos dieron de base usando una funcion que nos permite 
# utilizar cuatro propiedades o atributos.
print("Valor de FLAG:")
flag = funcionesUtiles.xor_4_bytes(clave1Byts, clave2, clave3, finalClaveBytes)
print(flag)
print(" -- ------------------------------------------------------------------- --")

# -- --------   ----------     ----------        -------------   ----------       -------------   ----------------
# He ocultado algunos datos usando XOR con un solo byte,
# pero ese byte es un secreto. No olvides decodificar primero desde hexadecimal.

print("Here is your seventh flag:")
# Tramos la variable que vamos a utilizar
hexFavorite = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
# La convertimos en bytes
byteFavorite = bytes.fromhex(hexFavorite)
# La imprimimos para ver su valor
print(byteFavorite)
# La pasarmos por un XOR con un valor fijo.
resultado_xor = funcionesUtiles.xor_a_una_cadenaDeBytes(byteFavorite, 16)
# imprimimos el resultado
print(resultado_xor)

# Algo así deberiamos hacer sino conocieramos el valor indicado de I:
# byteFavorite2 = bytes.fromhex(hexFavorite)
# for i in range(20):
#     print(i)
#     resultado_tres = funcionesUtiles.xor_a_una_cadenaDeBytes(byteFavorite2, i)
#     print(resultado_tres)
# imprimimos el resultado