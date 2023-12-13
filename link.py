#!/usr/bin/python3
import datetime;
ct = datetime.datetime.now()

seitenzahl = input("Bitte die maximale Seitenanzahl eingeben.")
link = input("Bitte den Seitenlink eingeben und die Seitenzahl durch '%a' (ohne '')ersetzen. ")
a = 1


with open("output.txt", "a") as f:
    print (ct, file=f)
    while a <= int(seitenzahl):
        string = link % (a)
        print (string, file=f)
        a = a + 1
    print ("--------------------", file=f)
    print ("", file=f)
    print ("", file=f)
    print ("", file=f)
