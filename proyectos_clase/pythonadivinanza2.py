"""Voy a hacer un juego de adivinar un número aleatorio entre el 0 y el 1000"""
"""Antés de comenzar la generación hay una breve introducción sobre si quieres jugar"""
"""Comenzando con la generación del número aleatorio que se tiene que adivinar"""
print("Juego de la adivinanza \nBuenas soy Adrián y he diseñado este juego")

jugar = input("¿Quieres jugar?: si (1), no (2)")
if jugar == 1:
    print("Adelante")
elif jugar == 2:
    print("Nos vemos")

import random
"""Aqui genero el número aleatorio con el random, pero le tengo que poner randint por que genera un número entero
y además se determina el número de intentos que quiere el usuario entre el 1 y el 6 haciendo un input"""
numero_random = random.randint(1,1000)
intentos = int(input("¿Cuántos intentos crees que necesitas entre el 1 y 6, genio?:")) 
"""Si intentos entra en el rango 1 y 6 te dice que esta correcto y procederá con el juego"""
if int(intentos) in range(0,7):
    print(f"Okey tienes {intentos}, me gusta ese número. Vamos a ello")
else:
    print("Demasiados intentos, no crees?")
    """Aqui le añado un exit al else para que cuando escribas mas intentos de los que te dice el rango te salga del programa"""
    exit()
"""Parte lógica del juego"""
"""Si acierta, el juego acaba. En cambio si el jugador escribe un número mayor el juego le devolverá que el número es más alto.
Y si el número es menor el juego le devolverá que el número es más bajo"""

for intento in range (1, intentos + 1):
        """Aqui creo una variable controlada "intento" que hace que el ciclo se repita exactamente los intentos que hayas escogido entre el 1 y el 6."""
        intento_user = int(input(f"Ingresa tu respuesta: "))
        """Aqui creo un input para que el usuario ingrese su respuesta a la adivinanza
        Luego hago unas condiciones sobre los resultados del usuario, si el usuario pone en el intento_user el número escogido de forma aleatoria, 
        el programa te felicita y te saca."""
        if intento_user == numero_random:
            print("¡Has acertado! Eres un genio")
            break
        elif int(intento_user) < numero_random:
            """Si el número escogido por el usuario es menor que el numero escogido por el programa, el juego te devolverá que el numero aleatorio es mayor"""
            print("El número es más alto")
        elif int(intento_user) > numero_random:
            """Aqui pasa lo mismo que antes pero le cambias que si el numero escogido por el usuario es mayor que el numero escogido aleatoriamente, el programa te devolverá que es menor"""
            print("El número es más bajo")
"""Parte final, si se te acaban los intentos que tu mismo has escogido el juego se acaba y te saca del programa"""
if intento == intentos:
     print("Se acabo el juego")