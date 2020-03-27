"""
    Controle de connaissance
    
    Guillaume LEAL DE ALMEIDA Groupe 27
    
    
    Question 1 : Fonction
    Créer une fonction appelée sup21 qui renvoie si un nombre est supérieur ou égal à 21
    >>> sup21(21)
    True
    >>> sup21(2)
    False
"""
def sup21(x):
    return x>=21

sup21(21)
sup21(2)

"""
    Question 2 : listes
    Créer une fonction `pairs` qui renvoie les éléments pairs d'une liste
"""
def pairs(l):
    return [i for i in l if i%2==0]

pairs([1,2,3])
 
"""
    Question 3 : Création de fonction
    Créer une fonction 'ajout4' qui prend en paramètre une liste et
    renvoie une nouvelle liste avec l'entier 4 ajouté à la fin.
    Vous ne devez pas modifier la liste de départ
"""
def ajout4(x):
    return x+[4]

ajout4([])
ajout4([1,2,4])
l = [1,2,3]
_ = ajout4(l)
l

"""
    Question 4
    Créer une fonction 'to_strings' qui pour un dictionnaire renvoie une liste de chaines de caractères
    au format suivant : 'clé:valeur'
    Exemple : pour {1:2} il faut renvoyer ['1:2']
"""
def to_strings(d):
    return [str(k)+":"+str(v) for k,v in zip(d.keys(),d.values())]

to_strings({1:2})
to_strings({})
to_strings({1:2,3:4})



"""
    Question5
    Créer une fonction 'extremites' qui renvoie les deux premiers et
    les deux derniers d'une liste : pour [1,2,3,4,5], renvoyer [1,2,4,5]
]
"""
def extremites(l):
    return l[0:2]+l[-2:]

extremites(['a', 'b', 'c', 'd', 'e'])

"""
    Question 6
    Créer une classe 'Mot' avec un attribut 'mot' et une methode 'comptelettre'
    qui prend en paramètre un caractère et renvoie le nombre d'occurences de ce
    caractère dans le mot. Attenton cela ne doit pas être sensible à la casse
"""
class Mot:
    def __init__(self, mot):
        self.mot = mot

    def comptelettre(self, lettre):
        return self.mot.count(lettre.lower())+ self.mot.count(lettre.upper())

mot = Mot('Bonjour')
mot.mot
mot.comptelettre('o')
mot.comptelettre('B') == mot.comptelettre('b') == 1
    
"""
    Question 7
    Créer une fonction 'tri_et_inverse' qui prend en paramètre une liste
    et renvoie (sans modifier la liste de départ) la liste triée et la liste départ mais dans le sens inverse
"""
def tri_et_inverse(x):
    return (sorted(x),list(reversed(x)))

maliste = [4,7,6]
tri_et_inverse(maliste)
maliste == [4,7,6]

"""
    Question 8: while et entrée utilisateur
    Completez fonction 'aller_a_paris' définie apres la doctest.
    Elle doit lire l'entrée utilisateur jusqu'a ce que l'utilisateur saisisse une chaine qui en
    minuscule vaut 'paris'.
    dans ce cas-là renvoyer "Paris" et le nombre de saisies utilisateur
    Pour les besoins du test j'utilise une petite astuce pour que vous n'ayez pas à saisir en vrai.
    >>> class fake_input:
    ...     def __init__(self, saisies):
    ...         self._iter = iter(saisies)
    ...     def __call__(self, *args, **kwargs):
    ...         return next(self._iter)
"""

class fake_input:
    def __init__(self, saisies):
         self._iter = iter(saisies)
         
    def __call__(self, *args, **kwargs):
        return next(self._iter)


def aller_a_paris(input_call=input):
    saisie = ''
    nb = 0
    while saisie.lower() != 'paris':
        saisie = input_call('Entrez le mot paris :')
        nb+=1
    return nb,'Paris'
    

list(aller_a_paris(input_call=fake_input(['Barcelone', "Madrid", "Paris"]))) 
aller_a_paris(input_call=fake_input(['Barcelone', "paris"]))

    

"""
    Question 9
    Créer un dictionnaire 'ville_nom_pays' qui contient en
    clefs 'Paris', 'Berlin', 'Madrid' et 'Moscou' et en
    valeur les noms des pays correspondants
"""

ville_nom_pays = {'Paris':'France',
                  'Berlin':'Allemagne',
                  'Madrid':'Espagne',
                  'Moscou':'Russie'
                  }


'Paris' in ville_nom_pays
'Espagne' in list(ville_nom_pays.values())
to_strings(ville_nom_pays)


"""
    Question 10
    - Créer une classe Pays dont les instances ont comme  attributs 'nom' (le nom du pays)
    et 'visa' (un visa est necessaire pour un ressortissant francais)
"""
class Pays:
    def __init__(self, nom, visa):
        self.nom = nom
        self.visa = visa


italie = Pays('Italie', False)
italie.visa
italie.nom


"""
    - Créer un dictionnaire 'ville_pays' avec les capitales comme clefs et les
    instances de pays comme valeurs. Pour Paris, Berlin, Mardrid et Moscou.
    Il faut un visa pour aller en Russie.
    Il ne faut pas de visa pour aller dans les trois autres pays
    >>> ville_pays['Moscou'].visa
    True
    >>> ville_pays['Berlin'].visa
    False
    
"""
France = Pays('France',False)
Allemagne = Pays('Allemagne',False)
Espagne = Pays('Espagne',False)
Russie = Pays('Russie',True)

ville_pays = {'Paris':France,
              'Berlin':Allemagne,
              'Madrid':Espagne,
              'Moscou':Russie
              }


ville_pays['Moscou'].visa
ville_pays['Berlin'].visa



if __name__ == "__main__":
    import doctest
    if True:
        doctest.testmod(verbose=True, optionflags=512)
    else:
        doctest.testmod(verbose=True)
