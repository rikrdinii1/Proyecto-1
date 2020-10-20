# Proyecto Nayelly y Ricardo. Trivia de los temas vistos en clase

# Variables Globales
list_jugadores = []
preguntas_juego = dict()

# Seleccion de Jugador y su nombre
def jugadores():
        
    for i in range(int(input("Seleccione el numero de jugadores: "))):
        i = input("Ingrese nombre del jugador: ")
        list_jugadores.append(i)


# Seleccion de nivel de dificultad del juego
def seleccion_dificultad():
    
    dificultad = (int(input("Seleccione la dificultad deseada 1, 2 o 3: ")))
    
    if dificultad == 1:
        preguntas_juego.update(preguntas_1)
    elif dificultad == 2:
        preguntas_juego.update(preguntas_2)
    elif dificultad == 3:
        preguntas_juego.update(preguntas_3)
    else:
        print('Nivel no identificado, vuelva a intentar')

# Reglas del Juego

# si la respuesta del usuario es igual al valor de la pregunta se suma un punto
# al jugador. 

# El jugador que al final tenga mas puntos gana. 
# si quedan empate se muestra mensaje de empate.

# Juego

# Se van mostrando pregunta por pregunta y se recibe la respuesta del jugador. T o F en mayusculas. la respuesta del jugador debe de ser convertida a mayusculas

# Puntaje del Juego

# Tal vez esta parte se quite porque está en las reglas del juego. 
# se van almacenando las respuestas de cada jugador

# Preguntas
# Preguntas de muestra, pendiente por sustituir por las verdaderas
preguntas_3 = {'pregunta1':True,
            'pregunta2':False,
            'pregunta3':True,
            'pregunta4':False,
            'pregunta5':True,
            'pregunta6':False,
            'pregunta7':True,
            'pregunta8':False,
            'pregunta9':True,
            'pregunta10':False,
            'pregunta11':True,
            'pregunta12':False,
            'pregunta13':True,
            'pregunta14':False,
            'pregunta15':True,
            'pregunta16':False,
            'pregunta17':True,
            'pregunta18':False,
            'pregunta19':True,
            'pregunta20':False,
            'pregunta21':True,
            'pregunta22':False,
            'pregunta23':True,
            'pregunta24':False,
            'pregunta25':True,
            'pregunta26':False,
            'pregunta27':True,
            'pregunta28':False,
            'pregunta29':True,
            'pregunta30':False}

preguntas_2 = {'pregunta1':True,
            'pregunta2':False,
            'pregunta3':True,
            'pregunta4':False,
            'pregunta5':True,
            'pregunta6':False,
            'pregunta7':True,
            'pregunta8':False,
            'pregunta9':True,
            'pregunta10':False,
            'pregunta11':True,
            'pregunta12':False,
            'pregunta13':True,
            'pregunta14':False,
            'pregunta15':True,
            'pregunta16':False,
            'pregunta17':True,
            'pregunta18':False,
            'pregunta19':True,
            'pregunta20':False}

preguntas_1 = {'pregunta1':True,
            'pregunta2':False,
            'pregunta3':True,
            'pregunta4':False,
            'pregunta5':True,
            'pregunta6':False,
            'pregunta7':True,
            'pregunta8':False,
            'pregunta9':True,
            'pregunta10':False}