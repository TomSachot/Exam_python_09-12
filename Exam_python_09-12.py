from colorama import init
init()
from colorama import Fore, Back, Style
import random

#mot1 = ["V", "O", "I", "T", "U", "R", "E"]
#mot2 = ["M", "O", "T", "E", "U", "R"]
#mot3 = ["F", "U", "S", "I", "L"]
#mot4 = ["R", "O", "U", "T", "E"]
#mot5 = ["B", "O", "U", "L", "E", "V", "A", "R", "D"]
#mot6 = ["P", "L", "A", "I", "N", "E"]
#mot7 = ["M", "A", "N", "O", "I", "R"]
#mot8 = ["G", "A", "D", "J", "E", "T"]
#mot9 = ["D", "Y", "N", "A", "M", "I", "T", "E"]
#mot10 = ["P", "O", "U", "R", "S", "U", "I", "T", "E"]

biblio_mots = ["VOITURE", "MOTEUR", "FUSIL", "ROUTE", "BOULEVARD", "PLAINE", "MANOIR", "GADJET", "DYNAMITE", "POURSUITE"]
tour = 0
motmystere = random.biblio_mots                          #Assigner un mot de la bibliothèque de façon aléatoire au mot mystère
motjoueur = int(input("Quel est le mot mystère ?")

for motmystere in range(1, 10):
    print(motmystere)
#Instaurer les 8 tentatives   
while (tour < 8):
    print(int(input("Quel est le mot mystère ?")))
    tour = tour + 1
    #Vérifier si les conditions de victoire sont réunies
    def verif ():
        #Quand le mot mystère est trouvé
        if (motjoueur = motmystere):
            print(Back.RED + motjoueur, end="")
            print("Bien joué ! C'est bien ",motjoueur," le mot mystère !")
        #Quand le mot du joueur n'est pas le même que le mot mystère
        if (motjoueur != motmystere):
            #Pour parcourir les lettres du mot du joueur et les comparer avec celles du mot mystère
            for i in range(1, 9):
                if ( = )
                    print(Back.RED
                if ( != )
                    print(Back.BLUE
                if ( =  )
                    print(Back.YELLOW
            print("Retentez ! Ce n'était pas ce mot-là...")
            
            