import curses, time

screen = curses.initscr()

curses.noecho()
curses.cbreak()
curses.start_color()
curses.curs_set(0)
screen.keypad(1)

animation = True
flicker = True

if animation == True:
	animation = 12

elif animation == False:
	animation = 0

if flicker == True:
	flicker = curses.A_BLINK

elif flicker == False:
	flicker = curses.A_STANDOUT

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

	tittle = (' ~ A P R E N D I E N D O   P Y T H O N 3 ~ ')
	screen.addstr(1, curses.COLS // 2 - len(tittle) // 2, tittle, curses.A_BOLD)

def options(num, opt):
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

			if num == 1:
				option = ('exit')
			else:
				option = ('')

			screen.border()
			up_down(num)
			escape = False

		elif key == 259:
			num += 1

			if num > 4:
				num = 4

			if num == 1:
				option = ('exit')
			else:
				option = ('')

			screen.border()
			up_down(num)
			escape = False

		elif key in [curses.KEY_ENTER, ord('\n'), 10]:
			escape = True
			curses.endwin()

			if option == ('exit'):
				main_exit(num)
				
			else:
				pass

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
		#screen.addstr(x - 3, 3, '|> Comenzar <|', curses.A_STANDOUT)
		screen.addstr(x - 3, 3, '              ')
		screen.addstr(x - 1, 3, 'Opciones      ')
		screen.addstr(x + 1, 3, 'Acerca De      ')
		screen.addstr(x + 3, 3, 'Salir      ')

		column = 2
		text = list("|> Comenzar")

		for i in text:
			column += 1
			screen.addstr(x - 3, column, i, curses.A_STANDOUT)
			screen.refresh()
			curses.napms(animation)

		screen.addstr(x - 3, 3, '|> Comenzar ', curses.A_STANDOUT | flicker)

	elif num == 3:
		screen.border()
		screen.addstr(x - 3, 3, 'Comenzar      ')
		screen.addstr(x - 1, 3, '            ')
		screen.addstr(x + 1, 3, 'Acerca De      ')
		screen.addstr(x + 3, 3, 'Salir      ')

		column = 2
		text = list('|> Opciones')

		for i in text:
			column += 1
			screen.addstr(x - 1, column, i, curses.A_STANDOUT)
			screen.refresh()
			curses.napms(animation)

		screen.addstr(x - 1, 3, '|> Opciones ', curses.A_STANDOUT | flicker)

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
			screen.addstr(x + 1, column, i, curses.A_STANDOUT)
			screen.refresh()
			curses.napms(animation)

		screen.addstr(x + 1, 3, '|> Acerca De ', curses.A_STANDOUT | flicker)

	elif num == 1:
		screen.addstr(x - 3, 3, 'Comenzar      ')
		screen.addstr(x - 1, 3, 'Opciones      ')
		screen.addstr(x + 1, 3, 'Acerca De     ')
		screen.addstr(x + 3, 3, '              ')

		column = 2
		text = list('|> Salir')

		for i in text:
			column += 1
			screen.addstr(x + 3, column, i, curses.A_STANDOUT)
			screen.refresh()
			curses.napms(animation)

		screen.addstr(x + 3, 3, '|> Salir ', curses.A_STANDOUT | flicker)

def main_space():
	x = curses.LINES // 2
	y = curses.COLS // 2

	space = ('- Presione ESPACIO -')
	screen.addstr(x, curses.COLS // 2 - len(space) // 2, space, curses.A_BLINK)

	escape = False

	while escape == False:
		screen.border()
		key = screen.getch(2, 1)

		if key == 32: # Espacio
			screen.erase()
			screen.refresh()
			escape = True
			options(4, '')

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
	screen.addstr(z + 3, 3, '|> Salir ', curses.A_STANDOUT)

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
			options(num, 'exit')
			escape = True
	

if __name__ == '__main__':
	curses.wrapper(main)