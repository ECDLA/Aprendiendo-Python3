import os
import time
from collections import Counter
from colorama import Cursor, init, Fore, Back

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