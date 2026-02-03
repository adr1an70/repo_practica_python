#Pokemon python.
"""Voy a recrear el inicio de pokemon rojo fuego, pero con algunas expeciones a mi gusto y conocimiento."""
nombre_pj= input("Bienvenido a pokemon rojo fuego, soy el profesor Oak. Antes de empezar, dime tu nombre: ")
print(f"Encantado de conocerte {nombre_pj}, este es un mundo habitado por criaturas llamadas pokemons. Son seres que coexisten con los humanos.")
print("Tu misión es convertirte en un maestro pokemon. Para ello, primero debes elegir tu pokemon inicial.")
print("Tienes tres opciones: Bulbasaur, Charmander o Squirtle.")
#Elección del tu pokemon inicial. 
pokemon_inicial= input("¿Cuál eliges?  1 (Bulbasaur) , 2 (Charmander) o 3 (Squirtle): ")

if int(pokemon_inicial) == 1:
    print("Has elegido a Bulbasaur, un pokemon de tipo planta/veneno. ¡Buena elección!")
    print("Quieres ponerle a Bulbasaur un apodo? (Digita 1 = Si o Digita 2 = No)")
    respuesta_apodo = input("Tu respuesta: ")
    if int(respuesta_apodo) == 1:
        apodo = input("¿Cuál es el apodo que le quieres poner a Bulbasaur? ")
        print(f"Has puesto a Bulbasaur el apodo de {apodo}.")
    if int(respuesta_apodo) == 2:
           print("Vale, Bulbasaur se quedo igual.")
elif int(pokemon_inicial) == 2:
    print("Has elegido a Charmander, un pokemon de tipo fuego. ¡Buena elección!")
    print("¿Quieres ponerle a Charmander un apodo?(Digita 1 = SI o Digita 2 = NO)")
    respuesta_apodo = input("Tu respuesta: ")
    if int(respuesta_apodo) == 1:
        apodo = input("¿Cuál es el apodo que le quieres poner a Charmander?")
        print(f"Has puesto a Charmander el apodo de {apodo}.")
        if int(respuesta_apodo) == 2:
           print("Vale, Charmander se quedo igual.")
elif int(pokemon_inicial) == 3:
    print("Has elegido a Squirtle, un pokemon de tipo agua. ¡Buena elección!")
    print("¿Quieres ponerle a Squirlte un apodo?(Digita 1 = SI o Digita 2 = NO)")
    respuesta_apodo = input("Tu respuesta: ")
    if int(respuesta_apodo) == 1 :
        apodo = input("¿Cuál es el apodo que le quieres poner a Squirtle?")
        print(f"Has puesto a Squirtle el apodo de {apodo}.")
    if int(respuesta_apodo) == 2:
           print("Vale, Squirtle se quedo igual.")
elif int(pokemon_inicial) == 4:
    print("Has elegido a Pikachu, un pokemon de tipo eléctrico. ¡Buena elección!")
    print("¿Quieres ponerle a Pikachu un apodo?(Digita 1 = SI o Digita 2 = NO)")
    respuesta_apodo = input("Tu respuesta: ")
    if int(respuesta_apodo) == 1:
        apodo = input("¿Cuál es el apodo que le quieres poner a Pikachu?")
        print(f"Has puesto a Pikachu el apodo de {apodo}.")
    if int(respuesta_apodo) == 2:
           print("Vale, Pikachu se quedo igual.")
else:
    print("Opción no válida. Por favor, elige entre Bulbasaur, Charmander o Squirtle.")



#Combate final pokemon contra Azul
print(f"Buenas {nombre_pj}, han pasado varios años desde que comenzaste tu camino, has conseguido derrotar al alto mando, ahora te falta derrotar al campeón de la Liga Pokemon Azul...")
print("Para enfrentar a Azul, necesitas que tu pokemon inicial alcance un nivel determinado. Me podrias decir a qué nivel has entrenado a tu pokemon inicial?")

nivel_pokemon = input("Introduce el nivel de tu pokemon inicial: ")
if nivel_pokemon >= "50":
    print("¡Felicidades! Tu pokemon inicial ha alcanzado el nivel 50, ahora puedes enfrentarte a Azul. ¡Buena suerte en tu batalla!")
    #Creación de tienda pokemon para comprar hiperpociones.
    print("Contra Azul necesitarás hiperpociones para curar a tus pokemons \n Entonces tendras que ir a las tiendas de objetos pokemon.")
    Tienda_pokemon =input("Quieres entrar a la tienda pokemon: Si (1) / No (2)")
    if int(Tienda_pokemon) == 1:
            comprar_objeto = input("Has entrado a la tienda Pokemon, te gustaria comprar hiperpociones? Si (1) / No(2):")
            if int(comprar_objeto) == 1:
                hiperpociones = input("¿Cuántas hiperpociones qeurrás?: ")
                print(f"Has comprado {hiperpociones} hiperpociones, usalas sabiamente")
            if int(comprar_objeto) == 2:
                print("¡Hasta la próxima!")
    if int(Tienda_pokemon) == 2:
        print("¡Hasta la próxima!")
elif nivel_pokemon < "50":
    print("Tu pokemon inicial no ha alcanzado el nivel necesario. Necesitas seguir entrenando antes de enfrentarte a Azul.")

#Has acabado el juego
print(f"Felicidades {nombre_pj}, has completado tu aventura en el mundo pokemon. ¡Eres ahora un maestro pokemon en la región de Kanto! Junto a tu pokemon has superado todos los desafíos y te has convertido en una leyenda.")
print("Gracias por jugar a Pokemon Rojo Fuego. ¡Hasta la próxima aventura!")