import curses

screen = curses.initscr()
curses.start_color()
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)

def tittle(screen, text):
	tittle = (text)
	screen.addstr(1, curses.COLS // 2 - len(tittle) // 2, tittle, curses.A_BOLD)

def flicker_center(screen, text, x):
	space = (text)
	screen.addstr(x, curses.COLS // 2 - len(space) // 2, space, curses.A_BLINK)

def animation(screen, text, line, off, flicker):
	column = 2
	text_animation = list(text)

	for i in text_animation:
		column += 1
		screen.addstr(line, column, i, curses.color_pair(1) | curses.A_STANDOUT)
		screen.refresh()
		curses.napms(off)

	screen.addstr(line, 3, str(text), curses.color_pair(1) | curses.A_STANDOUT | flicker)

def animation_off(screen, text, line, off, flicker):
	column = 2
	text_animation = list(text)

	for i in text_animation:
		column += 1
		screen.addstr(line, column, i, curses.color_pair(2))
		screen.refresh()
		curses.napms(off)

	screen.addstr(line, 3, str(text), curses.color_pair(2))


def error():
	screen.erase()
	screen.refresh()
	escape = True
	curses.endwin()

	screen.addstr("¡ERROR!\n", curses.COLOR_RED | curses.A_BOLD | curses.A_BLINK)
	escape = False

	while escape == False:

		x = screen.getch()

		if x == 10:
			escape = True
			curses.endwin()

		elif x == curses.KEY_RESIZE:
			screen.addstr("¡ERROR!\n", curses.A_BOLD | curses.A_BLINK)