import curses, run, opt1, fonts

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

#-------------------Colores--------------------
color_lyrics = COLOR_LYRICS[color_lyrics]
color_bold = COLOR_BOLD[color_bold]
cursor = CURSOR[cursor]

curses.init_pair(1, color_bold, color_lyrics)
#----------------------------------------------
#-------------------------------------------------------------------------------------

OPTION = {
	1: 'back',
	2: 'cursor',
	3: 'color',
	4: 'speed',
	5: 'flicker',
	6: 'animation'
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
	win.addstr('En proceso...', curses.A_BOLD)
	escape = False

	option = OPTION[num]

	while escape == False:
		curses.echo()
		key = win.getch(2, 2)

		if key == 10:
			opt(num, option)
			escape = True

		elif key == 27:
			opt(num, option)
			escape = True

		else:
			screen.erase()
			screen.refresh()
			escape = True
			curses.endwin()
			fonts.error()

def opt(num, opt):
	screen.border()
	escape = False
	fonts.tittle(screen, '~ O P C I O N E S ~')

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
				escape = True
				screen.erase()
				screen.refresh()
				curses.endwin()
				opt1.main(screen)

		elif key == curses.KEY_RESIZE:
			screen.erase()
			screen.refresh()
			escape = True
			curses.endwin()
			fonts.error()

def group():
	screen.addstr(x - 5, 3, 'Animacion     '),
	screen.addstr(x - 3, 3, 'Parpadeo      '),
	screen.addstr(x - 1, 3, 'Vel. Texto      '),
	screen.addstr(x + 1, 3, 'Colores      '),
	screen.addstr(x + 3, 3, 'Cursor       '),
	screen.addstr(x + 5, 3, 'Atras      ')

def up_down(num):
	x = curses.LINES // 2
	y = curses.COLS // 2

	fonts.tittle(screen, '~ O P C I O N E S ~')
	screen.border()
	group()

	if num == 6:
		line = x - 5
		screen.addstr(line, 3, '         ')
		fonts.animation(screen, '|> Animacion ', line, animation, flicker)

	elif num == 5:
		line = x - 3
		screen.addstr(line, 3, '          ')
		fonts.animation(screen, '|> Parpadeo ', line, animation, flicker)

	elif num == 4:
		line = x - 1
		screen.addstr(line, 3, '            ')
		fonts.animation(screen, '|> Vel. Texto ', line, animation, flicker)

	elif num == 3:
		line = x + 1
		screen.addstr(line, 3, '       ')
		fonts.animation(screen, '|> Colores ', line, animation, flicker)

	elif num == 2:
		line = x + 3
		screen.addstr(line, 3, '      ')
		fonts.animation(screen, '|> Cursor ', line, animation, flicker)

	elif num == 1:
		line = x + 5
		screen.addstr(line, 3, '     ')
		fonts.animation(screen, '|> Atras ', line, animation, flicker)

def main():
	screen.border()
	fonts.tittle(screen, '~ O P C I O N E S ~')
	opt(6, 'animation')