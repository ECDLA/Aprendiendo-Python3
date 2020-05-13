import nv0, curses

def main():
	try:
		lines = nv0.main('\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.\nHola, mundo. Esto es una prueba de mi codigo.', 10)
		nv0.main('Hola, mundo. Esto es una prueba de seguimiento para comprobar que se respetan los espacios de margenes.', 15)
	except:
		curses.endwin()
		print("Algo salio mal :(")
		raise