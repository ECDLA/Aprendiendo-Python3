import curses
import run

screen = curses.initscr()

curses.noecho()
curses.cbreak()
curses.start_color()
curses.curs_set(0)
screen.keypad(1)

animation = True
flicker = True

OPTION = {
	1: 'back',
	2: 'cursor',
	3: 'color',
	4: 'speed',
	5: 'flicker',
	6: 'animation'
}

#----------Animacion SI/NO----------
if animation == True:
	animation = 12

elif animation == False:
	animation = 0
#-----------------------------------

#----------Parpadeo SI/NO-----------
if flicker == True:
	flicker = curses.A_BLINK

elif flicker == False:
	flicker = curses.A_STANDOUT
#----------------------------------

x = curses.LINES // 2
y = curses.COLS // 2

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

def tittle_main():
	tittle = ('~ O P C I O N E S ~')
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

			if num > 6:
				num = 6

			option = OPTION[num]

			screen.border()
			up_down(num)
			escape = False

		elif key in [curses.KEY_ENTER, ord('\n'), 10]:
			escape = True
			curses.endwin()

			if option == ('back'):
				escape = True
				screen.erase()
				screen.refresh()
				curses.endwin()
				run.opt(3, 'options')

			elif option == ('cursor'):
				process(2)

			elif option == ('color'):
				process(3)

			elif option == ('speed'):
				process(4)

			elif option == ('flicker'):
				process(5)

			elif option == ('animation'):
				process(6)

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

	if num == 6:
		screen.border()
		screen.addstr(x - 5, 3, 'Animacion     ')
		screen.addstr(x - 3, 3, 'Parpadeo      ')
		screen.addstr(x - 1, 3, 'Vel. Texto      ')
		screen.addstr(x + 1, 3, 'Colores      ')
		screen.addstr(x + 3, 3, 'Cursor')
		screen.addstr(x + 5, 3, 'Atras      ')

		column = 2
		text = list("|> Animacion ")

		for i in text:
			column += 1
			screen.addstr(x - 5, column, i, curses.A_STANDOUT)
			screen.refresh()
			curses.napms(animation)

		screen.addstr(x - 5, 3, '|> Animacion ', curses.A_STANDOUT | flicker)

	elif num == 5:
		screen.border()
		screen.addstr(x - 5, 3, 'Animacion     ')
		screen.addstr(x - 3, 3, '              ')
		screen.addstr(x - 1, 3, 'Vel. Texto      ')
		screen.addstr(x + 1, 3, 'Colores      ')
		screen.addstr(x + 3, 3, 'Cursor')
		screen.addstr(x + 5, 3, 'Atras      ')

		column = 2
		text = list("|> Parpadeo")

		for i in text:
			column += 1
			screen.addstr(x - 3, column, i, curses.A_STANDOUT)
			screen.refresh()
			curses.napms(animation)

		screen.addstr(x - 3, 3, '|> Parpadeo ', curses.A_STANDOUT | flicker)

	elif num == 4:
		screen.border()
		screen.addstr(x - 5, 3, 'Animacion     ')
		screen.addstr(x - 3, 3, 'Parpadeo      ')
		screen.addstr(x - 1, 3, '            ')
		screen.addstr(x + 1, 3, 'Colores      ')
		screen.addstr(x + 3, 3, 'Cursor       ')
		screen.addstr(x + 5, 3, 'Atras      ')

		column = 2
		text = list('|> Vel. Texto ')

		for i in text:
			column += 1
			screen.addstr(x - 1, column, i, curses.A_STANDOUT)
			screen.refresh()
			curses.napms(animation)

		screen.addstr(x - 1, 3, '|> Vel. Texto ', curses.A_STANDOUT | flicker)

	elif num == 3:
		screen.border()
		screen.addstr(x - 5, 3, 'Animacion     ')
		screen.addstr(x - 3, 3, 'Parpadeo      ')
		screen.addstr(x - 1, 3, 'Vel. Texto      ')
		screen.addstr(x + 1 , 3, '             ')
		screen.addstr(x + 3, 3, 'Cursor        ')
		screen.addstr(x + 5, 3, 'Atras      ')

		column = 2
		text = list('|> Colores')

		for i in text:
			column += 1
			screen.addstr(x + 1, column, i, curses.A_STANDOUT)
			screen.refresh()
			curses.napms(animation)

		screen.addstr(x + 1, 3, '|> Colores ', curses.A_STANDOUT | flicker)

	elif num == 2:
		screen.border()
		screen.addstr(x - 5, 3, 'Animacion     ')
		screen.addstr(x - 3, 3, 'Parpadeo      ')
		screen.addstr(x - 1, 3, 'Vel. Texto      ')
		screen.addstr(x + 1, 3, 'Colores     ')
		screen.addstr(x + 3, 3, '                ')
		screen.addstr(x + 5, 3, 'Atras      ')

		column = 2
		text = list('|> Cursor ')

		for i in text:
			column += 1
			screen.addstr(x + 3, column, i, curses.A_STANDOUT)
			screen.refresh()
			curses.napms(animation)

		screen.addstr(x + 3, 3, '|> Cursor ', curses.A_STANDOUT | flicker)

	elif num == 1:
		screen.addstr(x - 5, 3, 'Animacion     ')
		screen.addstr(x - 3, 3, 'Parpadeo      ')
		screen.addstr(x - 1, 3, 'Vel. Texto      ')
		screen.addstr(x + 1, 3, 'Colores         ')
		screen.addstr(x + 3, 3, 'Cursor        ')
		screen.addstr(x + 5, 3, '         ')

		column = 2
		text = list('|> Atras')

		for i in text:
			column += 1
			screen.addstr(x + 5, column, i, curses.A_STANDOUT)
			screen.refresh()
			curses.napms(animation)

		screen.addstr(x + 5, 3, '|> Atras ', curses.A_STANDOUT | flicker)

def main():
	screen.border()
	tittle_main()
	opt(6, 'animation')