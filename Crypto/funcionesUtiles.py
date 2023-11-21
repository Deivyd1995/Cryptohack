# Recorre un string y lo convierte en un array
def stringToArrayByCharacters( palabra):
    letras = []
    for ch in range(0, len(palabra)):
        letras.append(palabra[ch])
    return letras
# Recorre un array y deuuelve el valor ASCII  correspondiente a cada item
def arrayToAcxii(converted):
    res = []
    for ch in range(0, len(converted)):
        res.append(ord(converted[ch]))
    return res

#  Realiza la operación XOR bit a bit entre el valor ASCII de cada carácter
#  en la cadena de entrada y un número base proporcionado. 
def xorToCadenaWithNumer(cadena, numeroBase):
    res = []
    for ch in cadena:
        res.append(ord(ch)^numeroBase )
    cadena_resultante = ''.join(chr(num) for num in res)
    
    return cadena_resultante

# Hacemos un XOR recorriendo dos cadenas de bytes, usando el principio de Asociacion
def xor_bytes(byte_str1, byte_str2):
    # Asegúrate de que ambas cadenas de bytes tengan la misma longitud
    if len(byte_str1) != len(byte_str2):
        raise ValueError("Las cadenas de bytes deben tener la misma longitud")

    # Realiza la operación XOR byte a byte
    resultado = bytes([a ^ b for a, b in zip(byte_str1, byte_str2)])
    
    return resultado

# Hacemos un XOR recorriendo cuatro cadenas de bytes, usando el principio de Asociacion
def xor_4_bytes(byte_str1, byte_str2, byte_str3, byte_str4):
    # Asegúrate de que todas las cadenas de bytes tengan la misma longitud
    if len(byte_str1) != len(byte_str2) or len(byte_str2) != len(byte_str3) or len(byte_str3) != len(byte_str4):
        raise ValueError("Todas las cadenas de bytes deben tener la misma longitud")

    # Realiza la operación XOR byte a byte para las 4 cadenas
    resultado = bytes([a ^ b ^ c ^ d for a, b, c, d in zip(byte_str1, byte_str2, byte_str3, byte_str4)])
    
    return resultado

# Hace un XOR a una cadena de Bytes a con un numero entero
def xor_a_una_cadenaDeBytes(bytesCadena, numero):
    # Realiza la operación XOR byte a byte
    resultado_xor = bytes([byte ^ numero for byte in bytesCadena])

    return resultado_xor

# Hace lo mismo que la funcion anterior pero en lugar de hacer el XOR con un unico numero, el valor del entero
# indicara cuantos ciclos for se realizaran y el numero del ciclo es el que usaremos para el XOR.
def xor_a_en_BucleDeCadenaDeBytes(bytesCadena, numero):
    for i in range(numero):
        print(i)
        resultado = xor_a_una_cadenaDeBytes(bytesCadena, i)
        print(resultado)

        return resultado