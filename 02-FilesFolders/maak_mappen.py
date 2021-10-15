import os
import io

bestand = open("klasgenoten.txt", "r")

# Eerste regel inlezen en opslaan in de variabele: tekst_regel
tekst_regel = bestand.readline()

# while loop gaat door zolang er iets in de variabele tekst_regel staat
while tekst_regel:
    # Let op: laat de code in de while loop 4 spaties inspringen!

    # De newline er af halen
    tekst_regel = tekst_regel.strip()

    # Maak een map met de naam
    os.mkdir(tekst_regel)

    # De regel op het scherm zetten:
    print("Map gemaakt met de naam: " + tekst_regel)

    # Volgende regel ophalen, zodat de while loop doorgaat
    tekst_regel = bestand.readline()