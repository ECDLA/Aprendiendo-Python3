from colorama import init, Cursor, Fore
from modules import options, system
import sys, tty, termios
import dialog as d

class options_menu:
	def opciones():
		d.menu.opciones()

	def empezar():
		d.menu.comenzar()

	def acerca():
		d.menu.acerca()

	def salir():
		d.menu.salir()


class inicio(options_menu):
	def __init__(self):
		d.inicio.empezar()

		#VARIABLES
		b_o = True #Bucle opciones

		ep = True #Empezar
		i_ar = True #Izquierda Arriba

		d_ab = False #Derecha abajo
		d_ar = False #Derecha arriba
		i_ab = False #Izquierda abajo

		#Entra en un blucle si BO es igual a Verdadero
		while b_o == True:
			#--------------------Captura entrada de teclas--------------------
			fd = sys.stdin.fileno()
			old_settings = termios.tcgetattr(fd)

			a = [0, 0, 0, 0, 0, 0]
			
			try:
			    tty.setraw(sys.stdin.fileno())
			    a[0]=ord(sys.stdin.read(1))
			    if a[0]==27:
			        a[1]=ord(sys.stdin.read(1))
			    if a[1]==91:
			        a[2]=ord(sys.stdin.read(1))
			    if (a[2]>=49 and a[2]<=54) or a[2]==91:
			        a[3]=ord(sys.stdin.read(1))
			    if a[3]>=48 and a[3]<=57:
			        a[4]=ord(sys.stdin.read(1))
			#------------------------------------------------------------------

			#Al finalizar la captura, almacena en 'a' la tecla seleccionada
			finally:

				#Ejecuta lo siguiente...
				termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

				#--------------------------------------------------------------
				#Si i_ar es igual a verdadero entonces...
				if i_ar == True:
					d.inicio.empezar()

					i_ar = True #Izquierda Arriba
					op_d_ar = True #Opcion derecha arriba

					d_ab = False #Derecha abajo
					d_ar = False #Derecha arriba
					i_ab = False #Izquierda abajo

					#Pero si la captura de tecla 'a' es igaul a 'Abajo', entonces...
					if a == [27, 91, 66, 0, 0, 0]:
						d.inicio.opciones()
						i_ab = True
						i_ar = False

					#Pero si la captura de tecla 'a' es igaul a 'Derecha', entonces...
					elif a == [27, 91, 67, 0, 0, 0]:
						d.inicio.acerca()
						i_ar = False
						d_ar = True

					#Pero si la captura de tecla 'a' es igaul a 'Enter', entonces...
					elif a == [13, 0, 0, 0, 0, 0]:
						options_menu.empezar()
						b_o = False

				#--------------------------------------------------------------
				elif i_ab == True:
					d.inicio.opciones()

					i_ab = True #Izquierda abajo

					d_ar = False #Derecha arriba
					d_ab = False #Derecha abajo
					i_ar = False #Izquierda Arriba

					#Si la captura de tecla 'a' es igaul a 'Arriba', entonces...
					if a == [27, 91, 65, 0, 0, 0]:
						d.inicio.empezar()
						i_ar = True
						i_ab = False
					
					#Pero si la captura de tecla 'a' es igaul a 'Derecha', entonces...
					elif a == [27, 91, 67, 0, 0, 0]:
						d.inicio.salir()
						d_ab = True
						i_ab = False

					elif a == [13, 0, 0, 0, 0, 0]: #Enter
						options_menu.opciones()
						b_o = False

				#--------------------------------------------------------------
				elif d_ar == True:
					d.inicio.acerca()

					d_ar = True #Derecha arriba

					d_ab = False #Derecha abajo
					i_ab = False #Izquierda abajo
					i_ar = False #Izquierda Arriba

					#Pero si la captura de tecla 'a' es igaul a 'Abajo', entonces...
					if a == [27, 91, 66, 0, 0, 0]:
						d.inicio.salir()
						d_ab = True
						d_ar = False

					#Pero si la captura de tecla 'a' es igaul a 'Izquierda', entonces...
					elif a == [27, 91, 68, 0, 0, 0]:
						d.inicio.empezar()
						i_ar = True
						d_ar = False

					#Pero si la captura de tecla 'a' es igaul a 'Enter', entonces...
					elif a == [13, 0, 0, 0, 0, 0]:
						options_menu.acerca()
						b_o = False

				#--------------------------------------------------------------
				elif d_ab == True:
					d.inicio.salir()

					d_ab = True #Derecha abajo

					d_ar = False #Derecha arriba
					i_ab = False #Izquierda abajo
					i_ar = False #Izquierda Arriba

					#Si la captura de tecla 'a' es igaul a 'Arriba', entonces...
					if a == [27, 91, 65, 0, 0, 0]:
						d.inicio.acerca()
						d_ar = True
						d_ab = False

					#Pero si la captura de tecla 'a' es igaul a 'Izquierda', entonces...
					elif a == [27, 91, 68, 0, 0, 0]:
						d.inicio.opciones()
						i_ab = True
						d_ab = False

					#Pero si la captura de tecla 'a' es igaul a 'Enter', entonces...
					elif a == [13, 0, 0, 0, 0, 0]:
						options_menu.salir()
						b_o = False
				#--------------------------------------------------------------