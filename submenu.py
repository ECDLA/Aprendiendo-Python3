import curses
import start, nv0, fonts

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
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
#----------------------------------------------
#-------------------------------------------------------------------------------------

TEXT = {
	1: str('- Presione ESPACIO -'),
	2: str('~ MODO ~'),
	3: str('Eligue tu modo')
}

OPTION = {
	5: 'game',
	4: 'normal',
	3: 'Hacking',
	2: 'web',
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

			if num > 5: num = 5

			option = OPTION[num]

			screen.border()
			up_down(num)
			escape = False

		elif key in [curses.KEY_ENTER, ord('\n'), 10]:
			escape = True
			curses.endwin()

			if option == ('exit'):
				main_exit(num)

			elif opt == ('game'):
				process(5)

			elif option == ('Hacking'):
				process(3)

			elif option == ('web'):
				process(2)

			elif option == ('normal'):
				nv0.main()

		elif key == curses.KEY_RESIZE:
			screen.erase()
			screen.refresh()
			escape = True
			curses.endwin()
			fonts.error()

def group():
	screen.addstr(x - 5, 3, 'Normal       '),
	screen.addstr(x - 3, 3, 'Hacking         '),
	screen.addstr(x - 1, 3, 'Web       '),
	screen.addstr(x + 1, 3, 'Videojuegos       '),
	screen.addstr(x + 3, 3, 'Atras      ')

def up_down(num):
	fonts.tittle(screen, TEXT[2])

	if num == 5:
		screen.border()
		line = x - 5
		group()

		screen.addstr(line, 3,  '               ')
		fonts.animation(screen, '|> Normal ', line, animation, flicker)

	elif num == 4:
		screen.border()
		line = x - 3 
		group()

		screen.addstr(line, 3,  '               ')
		fonts.animation_off(screen, '|> Hacking ', line, animation, flicker | curses.color_pair(2))

	elif num == 3:
		screen.border()
		line = x - 1
		group()

		screen.addstr(line, 3,  '             ')
		fonts.animation_off(screen, '|> Web ', line, animation, flicker | curses.color_pair(2))

	elif num == 2:
		screen.border()
		line = x + 1
		group()

		screen.addstr(line, 3,  '              ')
		fonts.animation_off(screen, '|> Videojuegos ', line, animation, flicker | curses.color_pair(2))


	elif num == 1:
		screen.border()
		line = x + 3
		group()
 
		screen.addstr(line, 3,  '      ')
		fonts.animation(screen, '|> Atras ', line, animation, flicker)

def main_space():
	z = curses.LINES // 2
	screen.addstr(z + 1, 3, '|> Seguir Demo ', curses.color_pair(1) | curses.A_STANDOUT)

	screen.border()
	screen.refresh()

	rows = 5
	cols = 36

	y = (curses.LINES - rows) // 2
	x = (curses.COLS - cols) // 2

	win = curses.newwin(rows, cols, y, x)

	win.box()

	win.move(2, 11)
	win.addstr(TEXT[3], curses.A_BOLD | curses.A_BLINK)

	escape = False

	while escape == False:
		curses.echo()
		key = win.getch(2, 2)

		if key == 10: escape = True

		elif key == 113:
			opt(5, 'normal')
			escape = True

def main():
	main_space()
	fonts.tittle(screen, TEXT[2])
	screen.erase()
	screen.refresh()
	escape = True
	opt(5, 'normal')

def main_exit(num):
	screen.erase()
	screen.refresh()
	curses.endwin()
	start.main(2)