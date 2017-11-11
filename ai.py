import random
import piskvorky

def tah_pocitace (herni_pole):
	while True:
		pozice = random.randrange (0,19)
		print("počítač si vybírá pozici", pozice)
		if herni_pole[pozice] != "-":
			print ("Políčko číslo ", pozice, "je obsazené, zkus jiné")
		else:
			return piskvorky.tah(herni_pole, "o", pozice)
