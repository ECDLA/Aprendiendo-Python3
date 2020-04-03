import importlib
import random
import os

importlib.import_module('.aprendiendo_python3.menu', package='..aprendiendo_python3')

AHORCADO = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''', 
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', 
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', 
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''', 
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', 
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', 
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
]

# Author: JCVBS / 67
# Es mejor de esta manera, mas legible.

WORDS = [
    'valoracion',
    'aprenderpython',
    'comida',
    'juego',
    'python',
    'web',
    'imposible',
    'variable',
    'curso',
    'volador',
    'cabeza',
    'reproductor',
    'mirada',
    'escritor',
    'billete',
    'lapicero',
    'celular',
    'valor',
    'revista',
    'gratuito',
    'disco',
    'voleibol',
    'anillo',
    'estrella',
]

def borrarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def buscarPalabraAleat(listaPalabras):
    return random.choice(WORDS)

def displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta):
    borrarPantalla()
    print(AHORCADO[len(letraIncorrecta)])
    print ("")
    fin = " "
    print ('Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print (letra, fin)
    print ("")
    espacio = '_' * len(palabraSecreta)
    print("Letras Correctas")
    for i in range(len(palabraSecreta)): # Remplaza los espacios en blanco por la letra bien escrita
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
    for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
        print (letra, fin)
    print ("")
    

def elijeLetra(algunaLetra):
    # Devuelve la letra que el jugador ingreso. Esta función hace que el jugador ingrese una letra y no cualquier otra cosa
    while True:
        print ('Adivina una letra:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print ('Introduce una sola letra.') 
        elif letra in algunaLetra:
            print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Elije una letra.')
        else:
            return letra

def empezar():
    # Esta funcion devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
    print('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')

print('A H O R C A D O')
letraIncorrecta = ""
letraCorrecta = ""
palabraSecreta = buscarPalabraAleat(WORDS)
finJuego = False
while True:
    displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
    # El usuario elije una letra.
    letra = elijeLetra(letraIncorrecta + letraCorrecta)
    if letra in palabraSecreta:
        letraCorrecta = letraCorrecta + letra
        # Se fija si el jugador ganó
        letrasEncontradas = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letraCorrecta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print ('¡Muy bien! La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
            finJuego = True
    else:
        letraIncorrecta = letraIncorrecta + letra
        # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
        if len(letraIncorrecta) == len(AHORCADO) - 1:
            displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
            print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
            finJuego = True
    # Pregunta al jugador si quiere jugar de nuevo
    if finJuego:
        if empezar():
            letraIncorrecta = ""
            letraCorrecta = ""
            finJuego = False
            palabraSecreta = buscarPalabraAleat(WORDS)
        else:
            break