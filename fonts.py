from colorama import Cursor, init, Fore, Back, Style
import time

# Author: JCVBS / 67
# Se reduce bastante codigo con esta constante, pues se repetie demasiado codigo.

COLORS = {
	'normal': Fore.RESET,
	'yellow': Fore.YELLOW,
	'red': Fore.RED,
	'blue': Fore.BLUE,
	'cyan': Fore.CYAN,
	'magenta': Fore.MAGENTA,
	'black': Fore.BLACK,
	'white': Fore.WHITE,
	'green': Fore.GREEN,
}

class delgada:
	init()

	def simple(color, line, column, text):
		# Aqui se mejora el codigo
		color = COLORS[color.lower()]

		print(Cursor.UP(line) + Cursor.FORWARD(column) + Style.DIM + color + text)
		print(Cursor.DOWN(line -2))

	def animado(color, line, column, Time, text):
		color = COLORS[color.lower()]
		text = list(text)
		column -= 1

		for i in text:
			if i == "&":
				column += 1
				print(Cursor.UP(line) + Cursor.FORWARD(column) + Style.DIM + color + str("."))
				print(Cursor.DOWN(line -2))
				time.sleep(Time + 0.5)

			elif i == "$":
				column += 1
				print(Cursor.UP(line) + Cursor.FORWARD(column) + Style.DIM + color + str(","))
				print(Cursor.DOWN(line -2))
				time.sleep(Time + 0.3)

			else:
				column += 1
				print(Cursor.UP(line) + Cursor.FORWARD(column) + Style.DIM + color + str(i))
				print(Cursor.DOWN(line -2))
				time.sleep(Time)

class normal:
	init()
	def simple(color, line, column, text):
		color = COLORS[color.lower()]

		print(Cursor.UP(line) + Cursor.FORWARD(column) + Style.NORMAL + color + text)
		print(Cursor.DOWN(line -2))

	def animado(color, line, column, Time, text):
		color = COLORS[color.lower()]
		text = list(text)
		column -= 1

		for i in text:
			if i == "&":
				column += 1
				print(Cursor.UP(line) + Cursor.FORWARD(column) + Style.NORMAL + color + str("."))
				print(Cursor.DOWN(line -2))
				time.sleep(Time + 0.5)

			elif i == "$":
				column += 1
				print(Cursor.UP(line) + Cursor.FORWARD(column) + Style.NORMAL + color + str(","))
				print(Cursor.DOWN(line -2))
				time.sleep(Time + 0.3)

			else:
				column += 1
				print(Cursor.UP(line) + Cursor.FORWARD(column) + Style.NORMAL + color + str(i))
				print(Cursor.DOWN(line -2))
				time.sleep(Time)

class negrita:
	init()
	def simple(color, line, column, text):
		color = COLORS[color.lower()]

		print(Cursor.UP(line) + Cursor.FORWARD(column) + Style.BRIGHT + color + text)
		print(Cursor.DOWN(line -2))

	def animado(color, line, column, Time, text):
		color = COLORS[color.lower()]
		text = list(text)
		column -= 1

		for i in text:
			if i == "&":
				column += 1
				print(Cursor.UP(line) + Cursor.FORWARD(column) + Style.BRIGHT + color + str("."))
				print(Cursor.DOWN(line -2))
				time.sleep(Time + 0.5)

			elif i == "$":
				column += 1
				print(Cursor.UP(line) + Cursor.FORWARD(column) + Style.BRIGHT + color + str(","))
				print(Cursor.DOWN(line -2))
				time.sleep(Time + 0.3)

			else:
				column += 1
				print(Cursor.UP(line) + Cursor.FORWARD(column) + Style.BRIGHT + color + str(i))
				print(Cursor.DOWN(line -2))
				time.sleep(Time)