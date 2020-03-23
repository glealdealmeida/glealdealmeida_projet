#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:44:26 2020

@author: guillaume
"""
from random import shuffle, randint
from time import sleep
regles =[]
regles.append( "Le but de ce jeu est d'obtenir 21 points, ou de s'en rapprocher le plus possible, et ainsi battre le croupier")
regles.append( "La mise de depart pour jouer est de 50$, il n'y a pas de mise maxiamle")
regles.append("Votre solde de depart est de 500$")
regles.append( "A chaque victoire votre mise de depart est doublé")
regles.append("Vous pouvez également miser 'paire' c'est-à-dire que votre première main est une paire")
regles.append("enfin le jeu s'arrete lorsque vous n'avez plus d'argent ou que vous taper 'fin' en debut de partie")
regles.append("Pour plus de simplicité l'As vaut 1")

couleur = ('Pique', 'Trefle', 'Carreau', 'Coeur')
valeur = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10')

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

def trier(paquet):
    shuffle(paquet)
    return paquet
trier(paquet)
print(paquet)


def joueur(paquet):
    val_joueur = 0
    t = 0
    paquet_joueur = paquet
    jouer = True
    i = randint(0,len(paquet_joueur))
    main_joueur.append(paquet_joueur[i])
    m = main_joueur[t]
    int_m = int(m[0])
    val_joueur = val_joueur + int_m
    t = 1
    while jouer is True and val_joueur<=21:
        i = randint(0,len(paquet_joueur))
        main_joueur.append(paquet_joueur[i])
        m = main_joueur[t]
        int_m = int(m[0])
        val_joueur = val_joueur + int_m
        print(main_joueur,val_joueur)
        print(i)
        t = t+1
        del(paquet_joueur[i])
        if val_joueur >21 :
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
                print("vous avez donc :",val_joueur," le croupier pour vous battre doit au moins vous egaler")
                sleep(2)
    return val_joueur
joueur(paquet)
val_joueur = 17

def croupier(paquet,val_joueur):
    jouer = True
    if val_joueur > 21:
        jouer = False
        victoire = croupier
        return victoire
    else :
        t = 0
        val_croupier = 0
        paquet_croupier = paquet
        i = randint(0,len(paquet_croupier))
        main_croupier.append(paquet_croupier[i])
        m = main_croupier[t]
        int_m = int(m[0])
        val_croupier = val_croupier + int_m
        t = 1
        while  jouer is True:
            print("le croupier joue")
            i = randint(0,len(paquet_croupier))
            main_croupier.append(paquet_croupier[i])
            m = main_croupier[t]
            int_m = int(m[0])
            val_croupier = val_croupier + int_m
            print("le croupier a tire :",main_croupier,"il a donc un total de :",val_croupier)
            t = t+1
            del(paquet_croupier[i])
            sleep(2)
            if val_croupier > 21 :
                print("le croupier s'arrete")
                victoire = "moi"
                return victoire
            elif val_croupier == 21 :
                print("le croupier s'arrete")
                victoire = "lui"
                return victoire
            elif val_croupier == val_joueur :
                print("le croupier s'arrete")
                victoire = "lui"
                return victoire
            elif val_croupier > val_joueur and val_croupier <=21 :
                print("le croupier s'arrete")
                victoire = "lui"
                return victoire
            
        return val_croupier, victoire
        
croupier(paquet,val_joueur)
            
def resultat(victoire,val_croupier,val_joueur):
    print("pour rappel, vous avez un total de :",val_joueur,"le croupier quand a lui a :",val_croupier)
    if victoire == "lui":
        print("victoire du croupier")
    else :
        print("vous avez gagnez")
            
val_joueur = 17
val_croupier = 21
victoire = "lui"
resultat(victoire,val_croupier,val_joueur)
