import io

# Zo open je een bestand om naar te schrijven 
bestand = open("test.txt", "w")

# Een tekst naar het bestand schrijven
bestand.write("Test 123!");  

# Vergeet bestand niet te sluiten!
bestand.close()