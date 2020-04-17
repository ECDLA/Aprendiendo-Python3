import options
import curses

screen = curses.initscr()

curses.noecho()
curses.cbreak()
curses.start_color()
curses.curs_set(0)
screen.keypad(1)

animation = True
flicker = True
color_bold = ('white')
color_lyrics = ('black')
cursor = 5

CURSOR = {
	1: '|> ',
	2: ' > ',
	3: '-> ',
	4: '- ',
	5: ''
}

COLOR_LYRICS = {
	'white': curses.COLOR_WHITE,
	'blue': curses.COLOR_BLUE,
	'red': curses.COLOR_RED,
	'black': curses.COLOR_BLACK,
	'yellow': curses.COLOR_YELLOW,
	'cyan': curses.COLOR_CYAN,
	'green': curses.COLOR_GREEN,
}

COLOR_BOLD = {
	'white': curses.COLOR_WHITE,
	'blue': curses.COLOR_BLUE,
	'red': curses.COLOR_RED,
	'black': curses.COLOR_BLACK,
	'yellow': curses.COLOR_YELLOW,
	'cyan': curses.COLOR_CYAN,
	'green': curses.COLOR_GREEN,
}

OPTION = {
	4: 'start',
	3: 'options',
	2: 'about',
	1: 'exit'
}

#----------------Animacion SI/NO----------------
if animation == True:
	animation = 12

elif animation == False:
	animation = 0
#-----------------------------------------------

#----------------Parpadeo SI/NO-----------------
if flicker == True:
	flicker = curses.A_BLINK

elif flicker == False:
	flicker = curses.A_STANDOUT
#----------------------------------------------

#-------------------Colores--------------------
color_lyrics = COLOR_LYRICS[color_lyrics]
color_bold = COLOR_BOLD[color_bold]
cursor = CURSOR[cursor]

curses.init_pair(1, color_bold, color_lyrics)
#----------------------------------------------

def process(num):
	z = curses.LINES // 2

	screen.border()
	screen.refresh()

	rows = 5
	cols = 36

	y = (curses.LINES - rows) // 2
	x = (curses.COLS - cols) // 2


	win = curses.newwin(rows, cols, y, x)

	win.box()

	win.move(2, 11)
	win.addstr('En proceso...', curses.A_BOLD)
	escape = False
	option = OPTION[num]

	while escape == False:
		curses.echo()
		key = win.getch(2, 2)
		win.move(2, 2)
		win.addstr('En proceso...', curses.A_BOLD)

		if key == 10:
			opt(num, option)
			escape = True

		elif key == 27:
			opt(num, option)
			escape = True

def error_main():
	screen.addstr("¡ERROR!\n", curses.COLOR_RED | curses.A_BOLD | curses.A_BLINK)
	escape = False

	while escape == False:

		x = screen.getch()

		if x == 10:
			escape = True
			curses.endwin()

		elif x == curses.KEY_RESIZE:
			screen.addstr("¡ERROR!\n", curses.color_pair(1) | curses.A_BOLD | curses.A_BLINK)

def tittle_main():
	x = curses.LINES // 2
	y = curses.COLS // 2

	tittle = ('~ A P R E N D I E N D O   P Y T H O N 3 ~')
	screen.addstr(1, curses.COLS // 2 - len(tittle) // 2, tittle, curses.A_BOLD)

def opt(num, opt):
	screen.border()
	escape = False
	tittle_main()

	up_down(num)

	option = str(opt)

	while escape == False:
		key = screen.getch(2, 1)

		if key == 258:
			num -= 1

			if num < 1:
				num = 1

			option = OPTION[num]

			screen.border()
			up_down(num)
			escape = False

		elif key == 259:
			num += 1

			if num > 4:
				num = 4

			option = OPTION[num]

			screen.border()
			up_down(num)
			escape = False

		elif key in [curses.KEY_ENTER, ord('\n'), 10]:
			escape = True
			curses.endwin()

			if option == ('exit'):
				main_exit(num)

			elif option == ('options'):
				escape = True
				screen.erase()
				screen.refresh()
				curses.endwin()
				options.main()

			elif option == ('about'):
				process(2)

			elif option == ('start'):
				process(4)

		elif key == curses.KEY_RESIZE:
			screen.erase()
			screen.refresh()
			escape = True
			curses.endwin()
			error_main()

def up_down(num):
	x = curses.LINES // 2
	y = curses.COLS // 2

	tittle_main()

	if num == 4:
		screen.border()
		screen.addstr(x - 3, 6, '              ')
		screen.addstr(x - 1, 3, 'Opciones      ')
		screen.addstr(x + 1, 3, 'Acerca De      ')
		screen.addstr(x + 3, 3, 'Salir      ')

		column = 2
		text = list('|> Comenzar ')

		for i in text:
			column += 1
			screen.addstr(x - 3, column, i, curses.color_pair(1) | curses.A_STANDOUT)
			screen.refresh()
			curses.napms(animation)

		screen.addstr(x - 3, 3, '|> Comenzar ', curses.color_pair(1) | curses.A_STANDOUT | flicker)

	elif num == 3:
		screen.border()
		screen.addstr(x - 3, 3, 'Comenzar      ')
		screen.addstr(x - 1, 3, '            ')
		screen.addstr(x + 1, 3, 'Acerca De      ')
		screen.addstr(x + 3, 3, 'Salir      ')

		column = 2
		text = list('|> Opciones ')

		for i in text:
			column += 1
			screen.addstr(x - 1, column, i, curses.color_pair(1) | curses.A_STANDOUT)
			screen.refresh()
			curses.napms(animation)

		screen.addstr(x - 1, 3, '|> Opciones ', curses.color_pair(1) | curses.A_STANDOUT | flicker)

	elif num == 2:
		screen.border()
		screen.addstr(x - 3, 3, 'Comenzar      ')
		screen.addstr(x - 1, 3, 'Opciones      ')
		screen.addstr(x + 1 , 3, '             ')
		screen.addstr(x + 3, 3, 'Salir      ')

		column = 2
		text = list('|> Acerca De')

		for i in text:
			column += 1
			screen.addstr(x + 1, column, i, curses.color_pair(1) | curses.A_STANDOUT)
			screen.refresh()
			curses.napms(animation)

		screen.addstr(x + 1, 3, '|> Acerca De ', curses.color_pair(1) | curses.A_STANDOUT | flicker)

	elif num == 1:
		screen.addstr(x - 3, 3, 'Comenzar      ')
		screen.addstr(x - 1, 3, 'Opciones      ')
		screen.addstr(x + 1, 3, 'Acerca De     ')
		screen.addstr(x + 3, 3, '              ')

		column = 2
		text = list('|> Salir')

		for i in text:
			column += 1
			screen.addstr(x + 3, column, i, curses.color_pair(1) | curses.A_STANDOUT)
			screen.refresh()
			curses.napms(animation)

		screen.addstr(x + 3, 3, '|> Salir ', curses.color_pair(1) | curses.A_STANDOUT | flicker)

def main_space():
	x = curses.LINES // 2
	y = curses.COLS // 2

	space = ('- Presione ESPACIO -')
	screen.addstr(x, curses.COLS // 2 - len(space) // 2, space, curses.A_BLINK)

	escape = False

	while escape == False:
		screen.border()
		key = screen.getch(2, 1)

		if key == 32:
			screen.erase()
			screen.refresh()
			escape = True
			opt(4, 'start')

		elif key == curses.KEY_RESIZE:
			screen.erase()
			screen.refresh()
			escape = True
			curses.endwin()
			error_main()

def main(screen):
	tittle_main()
	main_space()

def main_exit(num):
	z = curses.LINES // 2
	screen.addstr(z + 3, 3, '|> Salir ', curses.color_pair(1) | curses.A_STANDOUT)

	screen.border()
	screen.refresh()

	rows = 5
	cols = 36

	y = (curses.LINES - rows) // 2
	x = (curses.COLS - cols) // 2


	win = curses.newwin(rows, cols, y, x)

	win.box()

	win.move(2, 2)
	win.addstr('Presione ENTER para confirmar...', curses.A_BOLD | curses.A_BLINK)
	escape = False

	while escape == False:
		curses.echo()
		key = win.getch(2, 2)
		win.move(2, 2)
		win.addstr('Presione ENTER para confirmar...', curses.A_BOLD | curses.A_BLINK)

		if key == 10:
			escape = True

		elif key == 27:
			opt(num, 'exit')
			escape = True
	

if __name__ == '__main__':
	curses.wrapper(main)