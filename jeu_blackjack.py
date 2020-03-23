#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:53:51 2020

@author: guillaume
"""
from programme import regles,lamise,double,initialisation,trier,joueur,croupier,resultat
paquet_tri = []
paquet = []
main_joueur = []
main_croupier = []
solde = 500
print(regles)
jouer = True
while solde !=0 and jouer is True:
    paquet=initialisation(paquet)
    mise = int(input("entrez vortre mise (min 50)"))
    mise = lamise(mise,solde)
    solde = solde - mise
    pair = int(input("voulez vous miser 'paire' ? si oui entrez la mise (min 10) sinon entrez 0"))
    pair = double(pair,solde)
    paquet=trier(paquet)
    val_joueur = joueur(paquet)
    victoire,val_croupier = croupier(paquet,val_joueur)
    solde=resultat(victoire,val_croupier,val_joueur,solde,mise)   
    rep = int(input("le croupier dit :'voulez vous rejouer?'1 pour oui et 0 sinon"))
    if rep == 1:
        jouer is True
    else:
        print("le croupier dit :'au revoir et a bientot'")
        jouer is False
    
