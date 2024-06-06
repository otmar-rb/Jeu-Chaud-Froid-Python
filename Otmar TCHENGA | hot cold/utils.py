import sys
import time

# Les fonctions supplementaires utilisées

# Pour m'assurer que le joueur entre une valeur valide
def take_guessing(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entre une valeur valide(Un nombre): ")


# Si le joueur a fini continuer, on lui affiche un message personnalisé pour voir ce qu'il compte faire maintenant
def check_replay(case=""):
    time.sleep(2)
    if case == "goat":
        print("Non 😒")
        time.sleep(0.5)
        print("Je suis sur que tu as triché 😑! Essaie encore.")
        choice = take_guessing("1. On y va!\n2. 🙄 J'ai trop peur, je ne veux pas ")
    elif case == "tcho":
        choice = take_guessing("Chef ou bien Cheftaine. Tu peux pas t'arreter comme ca! 😁 \n1. T'as raison\n2. Non, c'est bon. ")
    else:
        choice = take_guessing("Encore une partie? 🎮 \n1. Let's go!\n2. Non, c'est bon. ")

    if choice == 1:
        return True
    else:
        sys.exit("Bon, quand on a peur...")

