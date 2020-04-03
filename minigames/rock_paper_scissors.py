from utils import clean_screen
import random
import time

OPTIONS = {
    # Option > Option
    'piedra': 'tijera',
    'papel': 'piedra',
    'tijera': 'papel',
}

banner = """
[i] Para salir del programa CONTROL-C

[ Piedra, Papel o Tijera!! ]

# Opciones:

|-piedra
|-papel
|-tijera
"""

while True:
    clean_screen()
    print(banner)

    option_user = input('> Elige una opcion: ')

    if option_user.lower() not in OPTIONS:
        print('\n> Opcion no valida intenta de nuevo...')
        time.sleep(5)
        continue

    option_random = random.choice(['piedra', 'papel', 'tijera'])

    if option_random == option_user:
        print(f'\n> { option_random } vs { option_user } | EMPATE')
        time.sleep(5)
        continue

    if OPTIONS[option_random] == option_user:
        print(f'\n> { option_random } vs { option_user } | PERDISTE')
        time.sleep(5)
        continue
    else:
        print(f'\n> { option_random } vs { option_user } | GANASTE')
        time.sleep(5)
        continue