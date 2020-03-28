from colorama import Cursor, init, Fore, Back, Style
import time

# Author: JCVBS / 67
# Se reduce bastante codigo con esta funcion, pues se repetie demasiado dicho codigo.

def color_filter(color):
	color = color.lower()
	if color == 'red': color = Fore.RED
	elif color == 'blue': color = Fore.BLUE
	elif color == 'cyan': color = Fore.CYAN
	elif color == "black": color = Fore.BLACK
	elif color == 'white': color = Fore.WHITE
	elif color == 'green': color = Fore.GREEN
	elif color == 'normal': color = Fore.RESET
	elif color == 'yellow': color = Fore.YELLOW
	elif color == 'magenta': color = Fore.MAGENTA

	return color

class delgada:
	init()

	def simple(color, line, column, text):
		color = color_filter(color)

		print(Cursor.UP(line) + Cursor.FORWARD(column) + Style.DIM + color + text)
		print(Cursor.DOWN(line -2))

	def animado(color, line, column, Time, text):
		color = color_filter(color)
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
		color = color_filter(color)

		print(Cursor.UP(line) + Cursor.FORWARD(column) + Style.NORMAL + color + text)
		print(Cursor.DOWN(line -2))

	def animado(color, line, column, Time, text):
		color = color_filter(color)
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
		color = color_filter(color)

		print(Cursor.UP(line) + Cursor.FORWARD(column) + Style.BRIGHT + color + text)
		print(Cursor.DOWN(line -2))

	def animado(color, line, column, Time, text):
		color = color_filter(color)
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