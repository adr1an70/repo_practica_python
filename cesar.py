#PARTE 1: FUNCIÓN BÁSICA
def cifrar_letra(letra, desplazamiento):
    if desplazamiento < 1 or desplazamiento > 25:
        raise ValueError("El desplazamiento debe estar entre el 1 y el 25 para que sea del abecedario")
#Convertir letra a código ASCII
    codigo = ord(letra)
#Aplicar desplazamiento con rotación 
    nuevo_codigo = 65 + (codigo - 65 + desplazamiento) % 26
#Convertir de nuevo a letra
    return chr(nuevo_codigo)

#CIFRADO DEL MENSAJE
def cifrar_mensaje(mensaje, desplazamiento):
    mensaje = mensaje.upper()
    resultado = ""

    for caracter in mensaje:
        if caracter.isalpha():  #Solo acepta letras
            resultado += cifrar_letra(caracter, desplazamiento)
        else:
            resultado += caracter
    return resultado

def descifrar_mensaje(mensaje, desplazamiento):
    #Como queremos cifrar usamos un desplazamiento inverso
    return cifrar_mensaje(mensaje, 26- desplazamiento)

#INTERACCIÓN CON EL USUARIO
if __name__ == "__main__":
    mensaje = input("Introduce el mensaje a cifrar:")

    while True:
        try:
            desplazamiento = int(input("Introduce el desplazamiento (1-25): "))
            if 1 <= desplazamiento <= 25:
                break
            else:
                print("Error: el numero debe estar entre 1 y 25.")
        except ValueError:
            print("Error:Debes introducir un valor valido")
            
mensaje_cifrado = cifrar_mensaje(mensaje, desplazamiento)
print(f"Mensaje cifrado", mensaje_cifrado)

mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, desplazamiento)
print("Mensaje descifrado:", mensaje_cifrado)