import random
import os
import time

endGame = False


def again():
    # Esta funcion devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
    print ('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def decorate():
    print("=" * 50)

def equal():
    print("Empate")
    time.sleep(2)
    start()

def winner():
    print("Felicidades, Ganó")
    

def looser():
    print("Más suerte la próxima")
    

options = ["Piedra", "Papel", "Tijera"]
def start():
    clear()
    decorate()
    print("Digite 1 para elegir Piedra")
    print("Digite 2 para elegir Papel")
    print("Digite 3 para elegir Tijera")
    decorate() 
    user = int(input("Digite su elección: "))
    user= user - 1
    cpu = random.choice(options)
    print("Usted elegió " + options[user])
    print("La CPU ha sacado " + cpu)
    if user != 0 and user != 1 and user != 2:
        print("La máquina gana por w")
        looser()
        return
    if cpu == "Piedra":
        print("    _______")
        print("---'   ____)")
        print("      (_____)")
        print("      (_____)")
        print("      (____)")
        print("---.__(___)")
        if user == 0:
            equal()
        elif user == 1:
            winner()
        elif user == 2:
            looser()
    elif cpu == "Papel":
        print("    _______")
        print("---'   ____)____")
        print("          ______)")
        print("          _______)")
        print("         _______)")
        print("---.__________)")
        if user == 0:
            looser()
        elif user == 1:
            equal()
        elif user == 2:
            winner()
    elif cpu == "Tijera":
        print("    _______")
        print("---'   ____)____")
        print("          ______)")
        print("       __________)")
        print("      (____)")
        print("---.__(___)")
        if user == 0:
            winner()
        if user == 1:
            looser()
        if user == 2:
            equal()
start()
