seitenummer = input("Bitte geben Sie die maxaimale Seitenzahl ein ")
b = input("Bitte geben Sie den Link ein und ersetzen Sie die Seitenzahl durch '%a' ")

a = 1

while a <= seitenummer:
	string = "http://erolord.com/images/215/2152641/%a.jpg" % (a)
	print (string)
	a = a + 1
