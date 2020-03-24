#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:44:26 2020

@author: guillaume

Le but de ce jeu est d'obtenir 21 points, ou de s'en rapprocher
le plus possible, et ainsi battre le croupier
La mise de depart pour jouer est de 50$, il n'y a pas de mise maxiamle
Votre solde de depart est de 500$
A chaque victoire votre mise de depart est doublé
Vous pouvez également miser 'paire' c'est-à-dire que votre première main est une paire
enfin le jeu s'arrete lorsque vous n'avez plus d'argent ou que vous taper 'fin' en debut de partie
Pour plus de simplicité l'As vaut 1


"""
from random import shuffle, randint
from time import sleep

couleurs = ("Pique", "Trefle", "Carreau", "Coeur")
valeur = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10")
cartes2valeus = {
    "as": 1,
    # etc b
    "roi": 10,
}


# ca en general vous allez
paquet_tri = []
paquet = []
main_joueur = []
main_croupier = []


def initialisation(paquet):
    for col in range(4):
        for val in range(13):
            nouvelle_carte = (valeur[val], couleur[col])
            paquet.append(nouvelle_carte)
    return paquet


initialisation(paquet)


def trier(paquet):  # melanger plutot ?
    shuffle(paquet)
    return paquet


trier(paquet)  # shuffle(paquet)  suffit
print(paquet)


def joueur(paquet):
    val_joueur = 0
    t = 0
    paquet_joueur = paquet
    jouer = True
    i = randint(0, len(paquet_joueur))
    main_joueur.append(paquet_joueur[i])
    m = main_joueur[t]
    int_m = int(m[0])
    val_joueur = val_joueur + int_m
    t = 1
    # nommez correctement vos variables
    while jouer is True and val_joueur <= 21:
        i = randint(0, len(paquet_joueur))
        main_joueur.append(paquet_joueur[i])  # random.choice
        m = main_joueur[t]  #
        int_m = int(m[0])
        val_joueur = val_joueur + int_m
        print(main_joueur, val_joueur)
        print(i)
        t = t + 1
        del paquet_joueur[i]
        if val_joueur > 21:
            tirage = False
            print("c'est perdu !")

        else:
            tirage = int(input("tirer ?, si oui taper 1, sinon 0"))
            if tirage == 1:
                jouer = True
                print("le croupier tire une carte")
                sleep(2)
            else:
                jouer = False
                print(
                    "vous avez donc :",
                    val_joueur,
                    " le croupier pour vous battre doit au moins vous egaler",
                )
                sleep(2)
            # Faites des fonctions plus petitest quitte a en appeler d'autres.
    return val_joueur


joueur(paquet)
val_joueur = 17

# pareil faites des fonctions
def croupier(paquet, val_joueur):
    jouer = True
    if val_joueur > 21:
        jouer = False
        victoire = croupier
        return victoire
    else:
        t = 0
        val_croupier = 0
        paquet_croupier = paquet
        i = randint(0, len(paquet_croupier))
        main_croupier.append(paquet_croupier[i])
        m = main_croupier[t]
        int_m = int(m[0])
        val_croupier = val_croupier + int_m
        t = 1
        while jouer is True:
            print("le croupier joue")
            i = randint(0, len(paquet_croupier))
            main_croupier.append(paquet_croupier[i])
            m = main_croupier[t]
            int_m = int(m[0])
            val_croupier = val_croupier + int_m
            print(
                "le croupier a tire :",
                main_croupier,
                "il a donc un total de :",
                val_croupier,
            )
            t = t + 1
            del paquet_croupier[i]
            # En fait vous auriez du utiliser un set pour modeliser le jeu de cartes
            # https://www.geeksforgeeks.org/python-set-pop/
            # main_croupier.add(paquet.pop())

            sleep(2)
            if val_croupier > 21:
                print("le croupier s'arrete")
                victoire = "moi"  # victoire = 'joueur'
                return victoire
            elif val_croupier == 21:  # elif superflus car early return
                print("le croupier s'arrete")
                victoire = "lui"  # viction = croupier
                return victoire
            elif val_croupier == val_joueur:
                print("le croupier s'arrete")
                victoire = "lui"
                return victoire
            elif val_croupier > val_joueur and val_croupier <= 21:
                print("le croupier s'arrete")
                victoire = "lui"
                return victoire
            # factoririzes le code le croupoer s'arret a chaque fois.

        return val_croupier, victoire


croupier(paquet, val_joueur)


# Erreur de desing vous avez enfoui la de l'entrée sortie.

# en gros:


def jeu(paquet):
    main_joueur = set()
    while True:
        saisie = int(input("voulez vous jouer ?"))
        if saisie:
            joueur_joue_tour(paquet, main_joueur)
        else:
            break

    main_croupier = set()
    while True:
        critere_darret = croupier_joue_tour(paquet, main_joueur, main_croupier)
        if critere_darret:
            break

    return gagnant(main_joueur, main_croupier)


if __name__ == "__main__":
    pass

# Est ce plus clair pour vous ? J'ai pris main jouer mais vous pouvez aussi utilier score a la place c'est juste
# qu'on peut facilement calculer le core en fonction de la main.


def resultat(victoire, val_croupier, val_joueur):
    print(
        "pour rappel, vous avez un total de :",
        val_joueur,
        "le croupier quand a lui a :",
        val_croupier,
    )
    if victoire == "lui":
        print("victoire du croupier")
    else:
        print("vous avez gagnez")


if __name__ == "__main__":

    val_joueur = 17
    val_croupier = 21
    victoire = "lui"
    resultat(victoire, val_croupier, val_joueur)
