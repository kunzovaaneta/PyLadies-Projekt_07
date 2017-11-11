import ai

def tah_hrace (herni_pole):
	while True:
		vlozena_pozice= input("Zvolte pozici 0-19 na kterou chcete hrát")
		try :
			pozice = int (vlozena_pozice)
			if pozice < 0 or pozice >19:
				print("prosím zadejte číslo v rozmezí 0-19")
			elif herni_pole[pozice] != "-":
				print ("Políčko číslo ", pozice, "je obsazené, zkus jiné")
			else:
				return tah(herni_pole,"x", pozice)
		except ValueError:
			print ("To nebylo číslo, zkuz to znovu")
	
			
def tah(herni_pole, znak, pozice):
	return herni_pole[:pozice] + znak + herni_pole[pozice + 1:]


def vyhodnot (herni_pole):
	if "xxx" in herni_pole:
		return "x"
	elif "ooo" in herni_pole:
		return "o"
	elif "-" not in herni_pole:
		return "!"
	else:
		return "-"

def piskvorky1d ():
	pole = 20*"-"
	na_tahu ="x"


	while True:
		print (pole)
		if na_tahu == "x":
			pole = tah_hrace(pole)
			na_tahu = "o"
		elif na_tahu == "o":
			pole = ai.tah_pocitace(pole)
			na_tahu = "x"
		
		if vyhodnot(pole) != "-":

			if vyhodnot(pole) == "x":
				print ("vyhrál hráč")
			elif vyhodnot(pole) == "o":
				print ("vyhrál počítač")
			elif vyhodnot(pole) == "!":
				print ("remize")
			break
		

piskvorky1d()
