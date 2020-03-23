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

paquet = []
paquet_valeur = []
main_joueur = []
main_croupier = []
solde = 500


def lamise(mise,solde):
    while mise < 50 or mise > solde:
        if mise < 50 :
            mise = int(input("le croupier n'accepete pas votre mise, car la mise est inferieur a 50"))
        else:
            mise = int(input("le croupier n'accepete pas votre mise, car vous n'avez pas assez"))
    return mise


def double(pair,solde):
    if pair == 0:
        print("vous n'avez pas choisi de miser pair, le croupier va commencer")
        return pair
    else: 
        while pair > solde or pair < 10:
            if pair > solde :
                pair = int(input("le croupier n'accepete pas votre mise, car vous n'avez pas assez"))
            else :
                pair = int(input("le croupier n'accepete pas votre mise, car la mise est inferieur a 10"))
        return pair




def initialisation(paquet):
    for col in range(4):
        for val in range(13):
            nouvelle_carte = (valeur[val], couleur[col])
            paquet.append(nouvelle_carte) 
    return paquet


def trier(paquet):
    shuffle(paquet)
    return paquet



def joueur(paquet):
    val_joueur = 0
    c = 0
    paquet_joueur = paquet
    jouer = True
    main_joueur.append(paquet_joueur[c])
    m = main_joueur[c]
    int_m = int(m[0])
    val_joueur = val_joueur + int_m
    c = 1
    while jouer is True and val_joueur<=21:
        main_joueur.append(paquet_joueur[c])
        m = main_joueur[c]
        int_m = int(m[0])
        val_joueur = val_joueur + int_m
        print(main_joueur,val_joueur)
        c = c+1
        del(paquet_joueur[c])
        if val_joueur >21 :
            tirage = False
            print("c'est perdu !")
            return val_joueur
        elif val_joueur >21 :
            tirage = False
            print("Vous avez 21")
            return val_joueur
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



def croupier(paquet,val_joueur):
    jouer = True
    if val_joueur > 21:
        jouer = False
        victoire = "lui"
        val_croupier = 0
        return victoire,val_croupier
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
                return victoire,val_croupier
            elif val_croupier == 21 :
                print("le croupier s'arrete")
                victoire = "lui"
                return victoire,val_croupier
            elif val_croupier == val_joueur :
                print("le croupier s'arrete")
                victoire = "lui"
                return victoire,val_croupier
            elif val_croupier > val_joueur and val_croupier < 21 :
                print("le croupier s'arrete")
                victoire = "lui"
                return victoire,val_croupier

            
def resultat(victoire,val_croupier,val_joueur,solde,mise):
    print("pour rappel, vous avez un total de :",val_joueur,"le croupier quand a lui a :",val_croupier)
    if victoire == "lui":
        print("victoire du croupier")
        solde = solde - mise
        print("votre solde estd de :",solde)
    else :
        print("vous avez gagnez")
        print("votre solde estd de :",solde)
 
