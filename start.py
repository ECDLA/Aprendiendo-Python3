import curses
import run, fonts
import prueba

screen = curses.initscr()

curses.noecho()
curses.cbreak()
curses.start_color()
curses.curs_set(0)
screen.keypad(1)

#------------------------------------Base de Datos------------------------------------
animation = True
flicker = True
color_bold = ('white')
color_lyrics = ('black')
cursor = 1

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
#-------------------------------------------------------------------------------------

TEXT = {
	1: str('- Presione ESPACIO -'),
	2: str('~ A P R E N D I E N D O   P Y T H O N 3 ~'),
	3: str('Presione ENTER para confirmar...')
}

OPTION = {
	4: 'start',
	3: 'options',
	2: 'about',
	1: 'exit'
}

x = curses.LINES // 2
y = curses.COLS // 2

def process(num):
	screen.border()
	screen.refresh()

	rows = 5
	cols = 36

	y = (curses.LINES - rows) // 2
	x = (curses.COLS - cols) // 2

	win = curses.newwin(rows, cols, y, x)

	win.box()

	win.move(2, 11)
	win.addstr('Proximamente...', curses.A_BOLD)
	escape = False
	option = OPTION[num]

	while escape == False:
		curses.echo()
		key = win.getch(2, 2)
		win.move(2, 2)
		win.addstr('Proximamente...', curses.A_BOLD)

		if key == 10:
			opt(num, option)
			escape = True

		elif key == 27:
			opt(num, option)
			escape = True

def opt(num, opt):
	screen.border()
	escape = False
	fonts.tittle(screen, TEXT[2])

	up_down(num)

	option = str(opt)

	while escape == False:
		key = screen.getch(2, 1)

		if key == 258:
			num -= 1

			if num < 1: num = 1

			option = OPTION[num]

			screen.border()
			up_down(num)
			escape = False

		elif key == 259:
			num += 1

			if num > 4: num = 4

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
				process(3)

			elif option == ('about'):
				prueba.main()

			elif option == ('start'):
				process(4)

		elif key == curses.KEY_RESIZE:
			screen.erase()
			screen.refresh()
			escape = True
			curses.endwin()
			fonts.error()

def group():
	screen.addstr(x - 3, 3, 'Iniciar sesion      '),
	screen.addstr(x - 1, 3, 'Crear cuenta        '),
	screen.addstr(x + 1, 3, 'Saguir en Demo      '),
	screen.addstr(x + 3, 3, 'Atras      ')

def up_down(num):
	fonts.tittle(screen, TEXT[2])

	if num == 4:
		screen.border()
		line = x - 3 
		group()

		screen.addstr(line, 3,  '               ')
		fonts.animation(screen, '|> Iniciar sesion ', line, animation, flicker)

	elif num == 3:
		screen.border()
		line = x - 1
		group()

		screen.addstr(line, 3,  '             ')
		fonts.animation(screen, '|> Crear cuenta ', line, animation, flicker)

	elif num == 2:
		screen.border()
		line = x + 1
		group()

		screen.addstr(line, 3,  '              ')
		fonts.animation(screen, '|> Seguir Demo ', line, animation, flicker)


	elif num == 1:
		screen.border()
		line = x + 3
		group()
 
		screen.addstr(line, 3,  '      ')
		fonts.animation(screen, '|> Atras ', line, animation, flicker)

def main_space():
	fonts.flicker_center(screen, TEXT[1], x)

def main():
	fonts.tittle(screen, TEXT[2])
	screen.erase()
	screen.refresh()
	escape = True
	opt(4, 'start')

def main_exit(num):
	screen.erase()
	screen.refresh()
	curses.endwin()
	run.opt(4, 'options')