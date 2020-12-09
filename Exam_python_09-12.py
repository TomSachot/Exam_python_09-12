tour = 0
mot1 = ["V", "O", "I", "T", "U", "R", "E"]
mot2 = ["M", "O", "T", "E", "U", "R"]
mot3 = ["F", "U", "S", "I", "L"]
mot4 = ["R", "O", "U", "T", "E"]
mot5 = ["B", "O", "U", "L", "E", "V", "A", "R", "D"]
mot6 = ["P", "L", "A", "I", "N", "E"]
mot7 = ["M", "A", "N", "O", "I", "R"]
mot8 = ["G", "A", "D", "J", "E", "T"]
mot9 = ["D", "Y", "N", "A", "M", "I", "T", "E"]
mot10 = ["P", "O", "U", "R", "S", "U", "I", "T", "E"]
motmystere = 
motjoueur = int(input("Quel est le mot mystère ?")

for motmystere in range(1, 10):
    print(motmystere)
    
while (tour < 8):
    print(int(input("Quel est le mot mystère ?")))
    tour = tour + 1
    def verif ():
        if (motjoueur = motmystere):
            print("Bien joué ! C'est bien ",motjoueur," le mot mystère !")
        if (motjoueur != motmystere):
            