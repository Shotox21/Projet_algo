import random


CISEAUX = "ciseaux"
FEUILLE = "feuille"
PIERRE = "pierre"

MON_SCORE = 0
SCORE_IA = 0
FIN = 5

CHOIX = "Faites votre choix parmi ces possibilités |pierre - feuille - ciseaux| : "

while FIN > MON_SCORE or FIN > SCORE_IA:

    choix_possibles = [PIERRE, FEUILLE, CISEAUX]
    while True:
        choix_joueur = input(CHOIX)
        if choix_joueur in (choix_possibles[0], choix_possibles[1], choix_possibles[2]):
            break

    choix_ia = random.choice(choix_possibles)

    print(f"Vous avez choisi {choix_joueur}. L'IA a choisi {choix_ia}")

    if (choix_joueur == FEUILLE and choix_ia == PIERRE) \
            or (choix_joueur == PIERRE and choix_ia == CISEAUX) \
            or (choix_joueur == CISEAUX and choix_ia == FEUILLE):
        MON_SCORE += 1
        print(f"Vous avez gagné ! Il y a {MON_SCORE} - {SCORE_IA}")

    elif (choix_joueur == FEUILLE and choix_ia == CISEAUX) \
            or (choix_joueur == PIERRE and choix_ia == FEUILLE) \
            or (choix_joueur == CISEAUX and choix_ia == PIERRE):
        SCORE_IA += 1
        print(f"Vous avez perdu ! Il y a {MON_SCORE} - {SCORE_IA}")
    else:
        print(f"Vous avez fait le même choix, pas de gagnant ! Il y a {MON_SCORE} - {SCORE_IA}")

    if FIN in (MON_SCORE, SCORE_IA):
        break
