from programme import regles,initialisation,trier,joueur,croupier,resultat
paquet_tri = []
paquet = []
main_joueur = []
main_croupier = []

print(regles)
initialisation(paquet)
joueur(paquet)
croupier(paquet,val_joueur)
resultat(victoire,val_croupier,val_joueur)
