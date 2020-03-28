from colorama import init, Cursor, Fore
from modules import fonts as f
from modules import system

class menu:
	def inicio():
		f.negrita.simple('normal', 25, 32, 'A P R E N D I E N D O  P Y T H O N')
		f.normal.simple('normal', 24, 44, 'By 0319-2N')
		f.normal.simple('yellow',  4, 83, 'Ver. 0.1')
		f.negrita.simple('green', 20, 28, '')

	def opciones():
		f.negrita.simple('normal', 25, 32, '           O P C I O N E S        ')
		f.normal.simple('normal', 24, 44, '          ')
		f.normal.simple('yellow',  4, 83, 'Ver. 0.1')
		f.negrita.simple('green', 20, 28, '')
		print(Cursor.UP(18) + Cursor.FORWARD(28) + Fore.GREEN + str('          '))
		print(Cursor.DOWN(18 -2))

		print(Cursor.UP(18) + Cursor.FORWARD(60) + Fore.GREEN + str('       '))
		print(Cursor.DOWN(18 -2))

		print(Cursor.UP(20) + Cursor.FORWARD(28) + Fore.BLUE + str('           '))
		print(Cursor.DOWN(20 -2))

		print(Cursor.UP(20) + Cursor.FORWARD(60) + Fore.GREEN + str('            '))
		print(Cursor.DOWN(20 -2))
		f.negrita.simple('green', 20, 28, '')

	def comenzar():
		pass

	def acerca():
		f.negrita.simple('normal', 25, 32, '          A C E R C A  D E        ')
		f.normal.simple('normal', 24, 44, '          ')
		f.normal.simple('yellow',  4, 83, 'Ver. 0.1')
		f.negrita.simple('green', 20, 28, '')
		print(Cursor.UP(18) + Cursor.FORWARD(28) + Fore.GREEN + str('          '))
		print(Cursor.DOWN(18 -2))

		print(Cursor.UP(18) + Cursor.FORWARD(60) + Fore.GREEN + str('       '))
		print(Cursor.DOWN(18 -2))

		print(Cursor.UP(20) + Cursor.FORWARD(28) + Fore.BLUE + str('           '))
		print(Cursor.DOWN(20 -2))

		print(Cursor.UP(20) + Cursor.FORWARD(60) + Fore.GREEN + str('            '))
		print(Cursor.DOWN(20 -2))
		f.negrita.simple('green', 20, 28, '')

	def salir():
		system.clear()

class inicio:
	def empezar():
		print(Cursor.UP(18) + Cursor.FORWARD(28) + Fore.GREEN + str('Opciones  '))
		print(Cursor.DOWN(18 -2))

		print(Cursor.UP(18) + Cursor.FORWARD(60) + Fore.GREEN + str('Salir  '))
		print(Cursor.DOWN(18 -2))

		print(Cursor.UP(20) + Cursor.FORWARD(28) + Fore.BLUE + str('> Empezar  '))
		print(Cursor.DOWN(20 -2))

		print(Cursor.UP(20) + Cursor.FORWARD(60) + Fore.GREEN + str('Acerca De   '))
		print(Cursor.DOWN(20 -2))

	def opciones():
		print(Cursor.UP(20) + Cursor.FORWARD(28) + Fore.GREEN + str('Empezar  '))
		print(Cursor.DOWN(20 -2))

		print(Cursor.UP(20) + Cursor.FORWARD(60) + Fore.GREEN + str('Acerca De   '))
		print(Cursor.DOWN(20 -2))

		print(Cursor.UP(18) + Cursor.FORWARD(28) + Fore.BLUE + str('> Opciones  '))
		print(Cursor.DOWN(18 -2))

		print(Cursor.UP(18) + Cursor.FORWARD(60) + Fore.GREEN + str('Salir  '))
		print(Cursor.DOWN(18 -2))

	def acerca():
		print(Cursor.UP(20) + Cursor.FORWARD(28) + Fore.GREEN + str('Empezar  '))
		print(Cursor.DOWN(20 -2))

		print(Cursor.UP(20) + Cursor.FORWARD(60) + Fore.BLUE + str('> Acerca De  '))
		print(Cursor.DOWN(20 -2))

		print(Cursor.UP(18) + Cursor.FORWARD(60) + Fore.GREEN + str('Salir  '))
		print(Cursor.DOWN(18 -2))

		print(Cursor.UP(18) + Cursor.FORWARD(28) + Fore.GREEN + str('Opciones  '))
		print(Cursor.DOWN(18 -2))

	def salir():
		print(Cursor.UP(20) + Cursor.FORWARD(28) + Fore.GREEN + str('Empezar  '))
		print(Cursor.DOWN(20 -2))

		print(Cursor.UP(20) + Cursor.FORWARD(60) + Fore.GREEN + str('Acerca De   '))
		print(Cursor.DOWN(20 -2))

		print(Cursor.UP(18) + Cursor.FORWARD(60) + Fore.BLUE + str('> Salir  '))
		print(Cursor.DOWN(18 -2))

		print(Cursor.UP(18) + Cursor.FORWARD(28) + Fore.GREEN + str('Opciones  '))
		print(Cursor.DOWN(18 -2))
