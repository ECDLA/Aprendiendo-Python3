"""

Antes estaba asi:

system = os.name

class clear:
	def __init__(self):
		global system

		if system == 'nt':
			os.system('cls')
		elif system == 'posix':
			os.system('clear')
		else:
			print("Lo lamento, tu terminal no es compatible :(")

Mejore el codigo a un funcion, creo inecesario crear una clase para
una funcion tan simple como limpiar la pantalla. 
Este comentario se eliminara dentro de poco, mas que nada para que vean el cambio.
De ser posible anoten sus nombres xd

"""

# Author: JCVBS / 67

import sys
import os

OPERATING_SYSTEM_TYPE = sys.platform

def clear():
	if OPERATING_SYSTEM_TYPE in ['linux', 'linux2']:
		os.system('clear')

	elif OPERATING_SYSTEM_TYPE in ['win32', 'cygwin', 'msys']:
		os.system('cls')

	else:
		print("Lo lamento, tu terminal no es compatible :(")
