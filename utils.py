# Author: JCVBS / 67

import sys
import os

OPERATING_SYSTEM_TYPE = sys.platform

def clean_screen():
	if OPERATING_SYSTEM_TYPE in ['linux', 'linux2']:
		os.system('clear')

	elif OPERATING_SYSTEM_TYPE in ['win32', 'cygwin', 'msys']:
		os.system('cls')

	else:
		print("Lo lamento, tu terminal no es compatible :(")
