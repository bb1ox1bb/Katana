# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                       #
# Modules   : RAR Brute Force   #
# Script by : LeSZO ZerO        #
# Date      : 28/02/2015        #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                   #
from core.design import *       #
from core.Setting import *      #
from core import Errors         #
from core import help           #
from core import ping           #
import sys                      #
d=DESIGN()                      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                     #
from lib.rarfile import *       #
import optparse                 #
import os                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaultarch="core/test/test.rar"
defaultdicc=DITIONARY_PASSWORDS
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #


def run(file,dictionary):
	global defaultarch,defaultdicc
	defaultarch=file
	defaultdicc=dictionary
	btrar(1)

def btrar(run):
	try:
		global defaultarch,defaultdicc
		if run!=1:
			actions=raw_input(d.prompt("fle/bruterar"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("file","yes","file with pass",defaultarch)
 			d.descrip("dict_1","yes","Dictionary pass",defaultdicc)
			print ""
			btrar(0)
		elif actions[0:8] == "set file":
			defaultarch=ping.update(defaultarch,actions,"file")
			d.change("file",defaultarch)
		elif actions[0:10] == "set dict_1":
			defaultdicc=ping.update(defaultdicc,actions,"dict_1")
			d.change("dict_1",defaultdicc)
		elif actions=="exit" or actions=="x":
			d.goodbye()
			exit()
		elif actions=="help" or actions=="h":
			help.help()
		elif actions=="back" or actions=="b":
			pass
		elif actions=="run"  or actions=="r":
			d.run()
			try:
				d.loading_file()
				Arch = open(defaultdicc,"r")
				if True:
					leeArchivo = Arch.readlines()
					for palabra in leeArchivo:
						palabraLlegada = palabra.split("\n")
						try:
							RARarch = RarFile(defaultarch)
							try:
								RARarch.extractall(pwd=str(palabraLlegada[0]))
								if True:
									ping.savetwo("BruteForceRAR",defaultarch,palabraLlegada[0])
									print "\n-"+Suf+" file Cracked with =",str(palabraLlegada[0])+"\n"
									return 1
							except:
								print " "+Alr+" Checking with ",str(palabraLlegada[0])
						except:
							Errors.Errors(event=sys.exc_info(), info=defaultarch)
			except:
				Errors.Errors(event=sys.exc_info(), info=defaultdicc)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info(), info=False)
	btrar(0)
