#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:53:51 2020

@author: guillaume
"""
from programme import regles,lamise,double,initialisation,trier,joueur,croupier,resultat,parid
from time import sleep
paquet = []
solde = 500

jeu = True
menu = True
while menu :
    print()
    if jeu :
        print("\\\\\MENU/////")
        print()
        print("1/ voulez vous que le croupier vous explique les regles ?")
        print()
        print ("2/ jouer")
        print()
        print ("3/ Quitter")
        choix = int(input("Faites votre choix :"))
        while choix > 3  or choix < 1 :
            choix = int(input("erreur! Faites votre choix :"))
        if choix == 1 :
            print("Option 1 : Le croupier s'installe pour vous expliquer")
            sleep(2)
            print(regles)
            print("le croupier reprend son soufle")
            sleep(2)
            choix = int(input("Faites votre choix :"))
            menu = True
        if choix == 2 :
            paquet=initialisation(paquet)
            mise = int(input("entrez vortre mise (min 50)"))
            mise = lamise(mise,solde)
            solde = solde - mise
            pair = int(input("voulez vous miser 'paire' ? si oui entrez la mise (min 10) sinon entrez 0"))
            pair = double(pair,solde)
            paquet=trier(paquet)
            val_joueur,pari,pari2,paquet = joueur(paquet)
            victoire,val_croupier,paquet = croupier(paquet,val_joueur)
            solde=resultat(victoire,val_croupier,val_joueur,solde,mise)
            solde=parid(pari,pari2,pair,solde)
            print(solde)
            if solde >= 50:
                jeu = True
            else :
                jeu = False
        if choix == 3:
            menu = False
            
    if jeu is False : 
        print("le croupier analyse votre solde")
        sleep(2)
        print("le croupier vous a depouille")
        print()
        print("vous n'avez plus assez")   
        menu = False

        
        
print("le croupier dit :'au revoir et a bientot'")
