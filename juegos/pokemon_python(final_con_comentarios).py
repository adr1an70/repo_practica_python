#Pokemon python.
"""Voy a recrear el inicio de pokemon rojo fuego, pero con algunas expeciones a mi gusto y conocimiento."""
"""He empezado usando unos prints que te dan la bienvenida al juego, como lo harian en el videojuego real"""
nombre_pj= input("Bienvenido a pokemon rojo fuego, soy el profesor Oak. Antes de empezar, dime tu nombre: ")
print(f"Encantado de conocerte {nombre_pj}, este es un mundo habitado por criaturas llamadas pokemons. Son seres que coexisten con los humanos.")
print("Tu misión es convertirte en un maestro pokemon. Para ello, primero debes elegir tu pokemon inicial.")
print("Tienes tres opciones: Bulbasaur, Charmander o Squirtle.")
#Elección del tu pokemon inicial. 
pokemon_inicial= input("¿Cuál eliges?  1 (Bulbasaur) , 2 (Charmander) o 3 (Squirtle): ") #He añadido a cada constante una variable para que el juego \n te pregunte por la información que deseas escoger.\n En este caso se refiere al inicial.
"""Inicia toda elección en el juego, ya sea pokemon, tienda, apodos, etc. Poniendo if, elif y else para que cada elección tenga consecuencias luego. 
En este ejemplo de los pokemon iniciales el juego te pregunta que pokemon quieres elegir con el input, y el if hace de condicional. 
Si tu digitas "x" número te escogera un pokemon en especifico. Después de la elección de cada Pokemon te preguntan con otro if si quieres añadirle un apodo a tu Pokemon. 
Luego en el elif se repite el mismo proceos pero con Pokemons distintos.
Al final con else, lo pongo para que si el jugador digita algo que no es un numero salga un error."""
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
if nivel_pokemon >= "50": #Aqui pongo que si el pokemon es nivel 50 o más, puedas enfrentarte a Azul.
    print("¡Felicidades! Tu pokemon inicial ha alcanzado el nivel 50, ahora puedes enfrentarte a Azul. ¡Buena suerte en tu batalla!")
    #Creación de tienda pokemon para comprar hiperpociones.
    print("Contra Azul necesitarás hiperpociones para curar a tus pokemons \n Entonces tendras que ir a las tiendas de objetos pokemon.")
#Añadir cuanto dinero tienes para comprar las hiperpociones
dinero = input("Cuanto dinero quieres tener para comprar hiperpociones: ") #Al poder enfrentarte a Azul, necesitas dinero para comprar hiperpociones. Por lo tanto el juego te añade un input para saber si quieres comprar, entrar a la tienda, etc.
if float(dinero) >= 10.5: #Escribi la variable float ya que el dinero puede ser decimal.
 print("Tienes dinero para una hiperpocion")
elif float(dinero) < 10.5:
 print("No tienes suficiente dinero")
#Eleccion de si quieres entrar a la tienda pokemon usando 1 Si y 2 No.
Tienda_pokemon =input("Quieres entrar a la tienda pokemon: Si (1) / No (2)") 
"""Aqui es muy parecido a la parte de la elección del pokemon inicial, ya que usé ifs y elifs para que cada elección tenga consecuencias. Y esas consecuencias son las siguientes:
Si el jugador digita 1, entra a la tienda pokemon y le pregunta si quiere comprar hiperpociones. Si el jugador digita 2, sale del juego.
Si el jugador digita algo que no es 1 o 2, el juego no hace nada."""
if int(Tienda_pokemon) == 1:
            comprar_objeto = input("Has entrado a la tienda Pokemon, te gustaria comprar hiperpociones? Si (1) / No(2):")
            if int(comprar_objeto) == 1:
                hiperpociones = input("¿Cuántas hiperpociones querrás?: ")
                print(f"Has comprado {hiperpociones} hiperpociones, usalas sabiamente")
            if int(comprar_objeto) == 2:
                print("¡Hasta la próxima!")
if int(Tienda_pokemon) == 2:
        print("¡Hasta la próxima!")
elif nivel_pokemon < "50":
     print("Tu pokemon inicial no ha alcanzado el nivel necesario. Necesitas seguir entrenando antes de enfrentarte a Azul.")

#Has acabado el juego
print(f"Felicidades {nombre_pj}, has completado tu aventura en el mundo pokemon. \n ¡Eres ahora un maestro pokemon en la región de Kanto!\n Junto a tu pokemon has superado todos los desafíos y te has convertido en una leyenda.")
print("Gracias por jugar a Pokemon Rojo Fuego. ¡Hasta la próxima aventura!")
"""Gracias a los ifs, elifs y inputs, he podido crear la etapa inicial y final de Pokemon donde tienes que hacer acciones decisivas, y como decisiones todas tiene consecuencias. \n Por eso añadi ifs y elifs. Los inputs los puse para poder hacer que el jugador pueda elegir directamente su propio camino."""