#python3
seitenzahl = input("Bitte die maximale Seitenanzahl eingeben.")
link = input("Bitte den Seitenlink eingeben und die Seitenzahl durch '%a' (ohne '')ersetzen. ")
a = 1

while a <= int(seitenzahl):
	string = link % (a)
	print (string)
	a = a + 1
