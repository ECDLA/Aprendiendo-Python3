from utils import clean_screen
import random
import time

IMAGES = [
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

def hanged():
    secret_word = random.choice(WORDS)
    wrong_letters = []
    correct_letters = []
    image_index = 0
    letter = ''

    while True:
        clean_screen()
        print(IMAGES[image_index])
        print('Letras correctas:', ', '.join(correct_letters))
        print('Letras incorrectas:', ', '.join(wrong_letters), end = '\n')

        # Si es la ultima imagen entra al if
        if len(IMAGES) - 1 == image_index:
            if input('\nQuieres jugar de nuevo? [S/n]: ').lower().startswith('s'):
                hanged()

            break
        else:     
            new_letter = input('\nAdivina una letra: ').lower()

        if new_letter in '1234567890':
            print('\nElije una letra no un numero.')
            time.sleep(3)

        elif len(new_letter) != 1:
            print('\nIntroduce una sola letra.') 
            time.sleep(3)

        elif new_letter == letter:
            print ('\nYa has elegido esa letra ¿Qué tal si pruebas con otra?')
            time.sleep(3)
        else:
            # Asigna las letras correctas e incorrectas a sus respectivas listas
            if new_letter not in secret_word:
                letter = new_letter
                wrong_letters.append(letter)
                image_index += 1
            else:
                letter = new_letter
                correct_letters.append(letter)
        
hanged()