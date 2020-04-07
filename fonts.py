import curses

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