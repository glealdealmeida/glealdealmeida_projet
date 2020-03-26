"""
ContrÃ´le de connaissances
Tout est Ã  faire en pur python respectez bien le nommage des variables

    Question 1 : Fonction
    CrÃ©er une fonction appelÃ©e sup21 qui renvoie si un nombre est supÃ©rieur ou Ã©gal Ã  21

    >>> sup21(21)
    True
    >>> sup21(2)
    False

    Question 2 : listes
    CrÃ©er une fonction `pairs` qui renvoie les Ã©lÃ©ments pairs d'une liste

    >>> pairs([1,2,3])
    [2]

    Question 3 : CrÃ©ation de fonction
    CrÃ©er une fonction 'ajout4' qui prend en paramÃ¨tre une liste et
    renvoie une nouvelle liste avec l'entier 4 ajoutÃ© Ã  la fin.
    Vous ne devez pas modifier la liste de dÃ©part

    >>> ajout4([])
    [4]
    >>> ajout4([1,2,4])
    [1, 2, 4, 4]
    >>> l = [1,2,3]
    >>> _ = ajout4(l)
    >>> l
    [1, 2, 3]

    Question 4
    CrÃ©er une fonction 'to_strings' qui pour un dictionnaire renvoie une liste de chaines de caractÃ¨res
    au format suivant : 'clÃ©:valeur'
    Exemple : pour {1:2} il faut renvoyer ['1:2']

    >>> to_strings({1:2})
    ['1:2']
    >>> to_strings({})
    []
    >>> to_strings({1:2,3:4})
    ['1:2', '3:4']

    Question5
    CrÃ©er une fonction 'extremites' qui renvoie les deux premiers et
    les deux derniers d'une liste : pour [1,2,3,4,5], renvoyer [1,2,4,5]

    >>> extremites(['a', 'b', 'c', 'd', 'e'])
    ['a', 'b', 'd', 'e']

    Question 6
    CrÃ©er une classe 'Mot' avec un attribut 'mot' et une methode 'comptelettre'
    qui prend en paramÃ¨tre un caractÃ¨re et renvoie le nombre d'occurences de ce
    caractÃ¨re dans le mot. Attenton cela ne doit pas Ãªtre sensible Ã  la casse

    >>> mot = Mot('Bonjour')
    >>> mot.mot
    'Bonjour'
    >>> mot.comptelettre('o')
    2
    >>> mot.comptelettre('B') == mot.comptelettre('b') == 1
    True

    Question 7
    CrÃ©er une fonction 'tri_et_inverse' qui prend en paramÃ¨tre une liste
    et renvoie (sans modifier la liste de dÃ©part) la liste triÃ©e et la liste dÃ©part mais dans le sens inverse

    >>> maliste = [4,7,6]
    >>> tri_et_inverse(maliste)
    ([4, 6, 7], [6, 7, 4])
    >>> maliste == [4,7,6]
    True

    Question 8: while et entrÃ©e utilisateur
    Completez fonction 'aller_a_paris' dÃ©finie apres la doctest.
    Elle doit lire l'entrÃ©e utilisateur jusqu'a ce que l'utilisateur saisisse une chaine qui en
    minuscule vaut 'paris'.
    dans ce cas-lÃ  renvoyer "Paris" et le nombre de saisies utilisateur

    Pour les besoins du test j'utilise une petite astuce pour que vous n'ayez pas Ã  saisir en vrai.

    >>> class fake_input:
    ...     def __init__(self, saisies):
    ...         self._iter = iter(saisies)
    ...     def __call__(self, *args, **kwargs):
    ...         return next(self._iter)
    ...
    ...
    >>> list(aller_a_paris(input_call=fake_input(['Barcelone', "Madrid", "Paris"]))) 
    [3, 'Paris']
    >>> aller_a_paris(input_call=fake_input(['Barcelone', "paris"]))
    (2, 'Paris')

    Question 9
    CrÃ©er un dictionnaire 'ville_nom_pays' qui contient en
    clefs 'Paris', 'Berlin', 'Madrid' et 'Moscou' et en
    valeur les noms des pays correspondants

    >>> 'Paris' in ville_nom_pays
    True
    >>> 'Espagne' in list(ville_nom_pays.values())
    True
    >>> to_strings(ville_nom_pays)
    ['Paris:France', 'Berlin:Allemagne', 'Madrid:Espagne', 'Moscou:Russie']

    Question 10
    - CrÃ©er une classe Pays dont les instances ont comme  attributs 'nom' (le nom du pays)
    et 'visa' (un visa est necessaire pour un ressortissant francais)


    >>> italie = Pays('Italie', False)
    >>> italie.visa
    False
    >>> italie.nom
    'Italie'
    
    - CrÃ©er un dictionnaire 'ville_pays' avec les capitales comme clefs et les
    instances de pays comme valeurs. Pour Paris, Berlin, Mardrid et Moscou.
    Il faut un visa pour aller en Russie.
    Il ne faut pas de visa pour aller dans les trois autres pays

    >>> ville_pays['Moscou'].visa
    True
    >>> ville_pays['Berlin'].visa
    False
    
    
"""



#Question 1
def sup21 (n) :
    if n>= 21 :
        return True
    else : 
        return False
sup21(22)

#Question 2
def pair(liste):
    return [k for k in liste if k%2==0]
            
liste =[1,2,3,4,5,6]
pair(liste)

#Question 3
def ajout4(liste):
    return liste+[4]
ajout4([])
ajout4([1,2,4])
li = [1,2,3]
_ = ajout4(li)
li

#Question 4
def to_strings(dictionnaire):
    return [str(k)+":"+str(v) for k,v in zip(dictionnaire.keys(),dictionnaire.values())]

to_strings({1:2})
to_strings({})
to_strings({1:2,3:4})
      
#Question 5
def extremites(liste):
    return liste[:2]+liste[-2]

extremites(['a', 'b', 'c', 'd', 'e'])

#Question 6
class Mot:
    def __init__(self, mot):
        self.mot = mot

    def comptelettre(self, l):
        return self.mot.count(l.lower())+ self.mot.count(l.upper())

mot = Mot('Bonjour')
mot.mot
mot.comptelettre('o')
mot.comptelettre('B') == mot.comptelettre('b') == 1

#Question 7
def tri_et_inverse(liste):
    return (sorted(liste),list(reversed(liste)))
maliste = [4,7,6]
tri_et_inverse(maliste)
maliste == [4,7,6]

#Question 8
class fake_input:
    def __init__(self, saisies):
         self._iter = iter(saisies)
         
    def __call__(self, *args, **kwargs):
        return next(self._iter)
def aller_a_paris(input_call=input):
    entre = ''
    n = 0
    while entre.lower() != 'paris':
        entre = input_call('Entrez le mot paris :')
        n = n + 1
    return n,'Paris'
    
list(aller_a_paris(input_call=fake_input(['Barcelone', "Madrid", "Paris"]))) 
aller_a_paris(input_call=fake_input(['Barcelone', "paris"]))

#Question 9
ville_nom_pays = {
        'Paris':'France', 
        'Berlin':'Allemagne', 
        'Madrid':'Espagne',
        'Moscou':'Russie'
        }
'Paris' in ville_nom_pays
'Espagne' in list(ville_nom_pays.values())
to_strings(ville_nom_pays)

#Question 10
class Pays:
    def __init__(self, nom, visa):
        self.nom = nom
        self.visa = visa


italie = Pays('Italie', False)
italie.visa
italie.nom
Russie = Pays('Russie',True)
Allemagne = Pays('Allemagne',False)
Espagne = Pays('Espagne',False)
France = Pays('France',False)
ville_pays = {'Paris':France,'Berlin':Allemagne,'Madrid':Espagne,'Moscou':Russie}
ville_pays['Moscou'].visa
ville_pays['Berlin'].visa



if __name__ == "__main__":
    import doctest
    if True:
        doctest.testmod(verbose=True, optionflags=512)
    else:
        doctest.testmod(verbose=True)
