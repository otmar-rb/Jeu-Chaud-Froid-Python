import math
import sys
from random import randint
from utils import *

is_playing = True

while is_playing:

    min = randint(0, 40) #Le debut de l'intervalle
    max = randint(min, 200) #La fin de l'intervalle
    
    total_attempts = int((max - min) / 8)

    past_attempts = [] # pour garder la trace des anciens coups

    print("\n🏁 LET'S GO! BIENVENUE AU JEU DU \"CHAUD OU FROID\"! 🏁")
    print(f"Je pense à un nombre 🎲 entre {min} et {max}.")
    print(f"De ton coté, tu as {total_attempts} tentatives pour trouver le nombre: ")

    mystery_number = randint(min, max)
    for attempt in range(1, total_attempts + 1):

        guessing = take_guessing("Quelle est ta supposition ❓ ")
        difference = abs(mystery_number - guessing)

        if difference == 0:
            if attempt == 1:
                print("🤯 LE G.O.A.T ABSOLU 🙇! Tu as trouvé le bon nombre du premier coup!")
                # Pour verifier si le joueur veut rejouer
                is_playing = check_replay("goat")
                break
            else:
                print(f"Bien joué! tu as trouvé! En {attempt} tentatives")
                is_playing = check_replay()
                break
        else:
            if difference < 3:
                print("🌶 Là c'est très chaud, bouillant même! 🌶")
            elif difference < 6:
                print("C'est chaud! 🤒")
            elif difference < 11:
                print("C'est Tiède 🤙")
            elif difference < 21:
                print("C'est froid! 🤧")
            else:
                print("Tu es loinnn! C'est hyper froid! 🧊🧊")
            past_attempts.append(guessing)
            print(f"Tentatives restantes: {total_attempts - attempt}")
            print(f"Tentatives passées : {past_attempts}")

        if attempt == total_attempts:
            print(f"😬 Désolé, tu as épuisé tes tentatives. Le nombre secret était {mystery_number}.")
            is_playing = check_replay("tcho")
            break
