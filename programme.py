#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:44:26 2020

@author: guillaume
"""
from random import shuffle
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
valeur = ('As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi')
cartes2valeus = {
    "As": 1,
    "2": 2,
    '3':3,
    '4':4, 
    '5':5, 
    '6':6, 
    '7':7, 
    '8':8, 
    '9':9, 
    '10':10, 
    'Valet':10, 
    'Dame':10, 
    'Roi':10
     }

paquet = []
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
        while pair > solde  or pair < 10 and pair>0:
            if pair > solde :
                pair = int(input("le croupier n'accepete pas votre mise, car vous n'avez pas assez"))
            elif pair < 10 and pair != 0:
                pair = int(input("le croupier n'accepete pas votre mise, car la mise est inferieur a 10"))
                
        return pair




def initialisation(paquet):
    print("le croupier prend un jeu de carte")
    sleep(2)
    for col in range(4):
        for val in range(13):
            nouvelle_carte = (valeur[val], couleur[col])
            paquet.append(nouvelle_carte) 
    return paquet


def melanger(paquet):
    print("le croupier melange le jeu de carte")
    sleep(2)
    shuffle(paquet)
    return paquet



def joueur(paquet):
    val_joueur = 0
    c = 0
    paquet_joueur = paquet
    main_joueur = []
    main_joueur2 = []
    jouer = True
    main_joueur.append(paquet_joueur[c])
    m = main_joueur[c]
    val = cartes2valeus[m[0]]
    val_joueur = val_joueur + val
    pari = m[0]
    del(paquet[c])
    c = 1
    main_joueur2.append(paquet_joueur[c])
    m = main_joueur2[0]
    pari2=m[0]
    c = 1
    sleep(2)
    while jouer is True and val_joueur<=21:
        main_joueur.append(paquet_joueur[c])
        m = main_joueur[c]
        val = cartes2valeus[m[0]]
        val_joueur = val_joueur + val
        print(main_joueur,val_joueur)
        del(paquet_joueur[c])
        del(paquet[c])
        c = c+1
        sleep(2)
        if val_joueur >21 :
            tirage = False
            print("c'est perdu !")
            del(c)
            del(main_joueur)
            del(paquet_joueur)
            del(main_joueur2)
            return val_joueur,pari,pari2,paquet
        elif val_joueur >21 :
            tirage = False
            print("Vous avez 21")
            del(c)
            del(main_joueur)
            del(paquet_joueur)
            del(main_joueur2)
            return val_joueur,pari,pari2,paquet
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
                del(c)
                del(main_joueur)
                del(main_joueur2)
                del(paquet_joueur)
                return val_joueur,pari,pari2,paquet



def croupier(paquet,val_joueur):
    jouer = True
    if val_joueur > 21:
        jouer = False
        victoire = "lui"
        val_croupier = 0
        return victoire,val_croupier,paquet
    else :
        c = 0
        val_croupier = 0
        main_croupier=[]
        paquet_croupier = paquet
        main_croupier.append(paquet_croupier[c])
        m = main_croupier[c]
        del(paquet[c])
        val = cartes2valeus[m[0]]
        val_croupier = val_croupier + val
        c = 1
        sleep(2)
        while  jouer is True:
            print("le croupier joue")
            main_croupier.append(paquet_croupier[c])
            m = main_croupier[c]
            val = cartes2valeus[m[0]]
            val_croupier = val_croupier + val
            print("le croupier a tire :",main_croupier,"il a donc un total de :",val_croupier)
            del(paquet_croupier[c])
            del(paquet[c])
            c = c+1
            sleep(2)
            if val_croupier > 21 :
                print("le croupier s'arrete")
                victoire = "joueur"
                del(c)
                del(main_croupier)
                del(paquet_croupier)
                return victoire,val_croupier,paquet
            elif val_croupier == 21 :
                print("le croupier s'arrete")
                victoire = "lui"
                del(c)
                del(main_croupier)
                del(paquet_croupier)
                return victoire,val_croupier,paquet
            elif val_croupier == val_joueur :
                print("le croupier s'arrete")
                victoire = "lui"
                del(c)
                del(main_croupier)
                del(paquet_croupier)
                return victoire,val_croupier,paquet
            elif val_croupier > val_joueur and val_croupier < 21 :
                print("le croupier s'arrete")
                victoire = "lui"
                del(c)
                del(main_croupier)
                del(paquet_croupier)
                return victoire,val_croupier,paquet

            
def resultat(victoire,val_croupier,val_joueur,solde,mise):
    print("pour rappel, vous avez un total de :",val_joueur,"le croupier quand a lui a :",val_croupier)
    if victoire == "lui":
        print("victoire du croupier")
        solde = solde
        sleep(2)
        return solde
    else :
        print("vous avez gagnez")
        solde = solde + mise*2
        sleep(2)
        return solde
    
def parid(pari,pari2,pair,solde):
    if pair != 0:
        if pari == pari2:
            solde = solde + pair
            print("votre solde est de :",solde)
            return solde
        elif pari != pari2:
            solde = solde - pair
            print("votre solde est de :",solde)
            return solde
    else:
        solde = solde
        print("votre solde est de :",solde)
        return solde

