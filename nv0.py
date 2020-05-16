import curses

screen = curses.initscr()

def dialogues(text, time):
	screen.erase()
	screen.border()

	lines = curses.LINES
	cols = curses.COLS
	col = 1
	line = 2
	counter = 0
	counter_line = 0
	num = 0
	x = ''
	paso = False

	for i in list(text):
		screen.refresh()
		counter += 1

		if counter > (cols - 6):
			counter = 0
			counter_line += 1
			line += 1
			col = 2
		else:
			col += 1

		if i == '\n':
			line += 1
			col = 1
			counter = 0
			counter_line += 1

		if counter_line > (lines - 6):
			counter_line = 0
			screen.move(line + 1, cols - len('Suguiente...') - 1)
			screen.addstr('Siguiente...')
			screen.getch()
			screen.erase()
			screen.border()
			col = 2
			line = 2

		if (col + len(x)) > (cols - 3):
			screen.move(line, col + 1)
			screen.addstr('-')
			screen.getch()
			line += 1
			col = 2
			counter = 0
		
		screen.move(line, col)
		screen.addstr(i)
		curses.napms(time)

		screen.refresh()
		screen.border()

	screen.move(lines - 2, cols - len('Continuar...') - 1)
	screen.addstr('Continuar...')
	screen.getch()
	curses.endwin()

	return lines, cols, x

def main():
	dialogues('\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.', 5)
	dialogues('Hola, mundo. Esto es una prueba de seguimiento para comprobar que se respetan los espacios de margenes.', 15)