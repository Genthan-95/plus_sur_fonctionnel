# Exercice 1

def au_carre(n):
    return n ** 2

def addition(a, b):
    return a + b

nombres = [1, 2, 3, 4, 5]
somme_totale = sum(nombres)
carres = [au_carre(n) for n in nombres]

print("La somme totale est", somme_totale)
print("La somme de 2 + 4 est :", addition(2, 4))
print("Les carrés de la liste sont :", carres)
print("Le carré de 2 est :", au_carre(2))

# Exercice 2

def multiplier_par(n):
    return lambda x: x * n

double = multiplier_par(2)
triple = multiplier_par(3)

print("Le double de 5 est :", double(5))
print("Le triple de 5 est :", triple(5))

# Exercice 3

def compter_mots():
    def compteur(liste_mots):
        return sum(1 for mot in liste_mots if len(mot) > 5)
    return compteur

mots = ["pomme", "banane", "cerise", "pain", "lait", "avocat"]
mots_filtrés = [mot for mot in mots if mot.startswith("a")]
compteur = compter_mots()

print("Les mots qui commencent par 'a' sont :", mots_filtrés)
print("Le nombre de mots de plus de 5 lettres est :", compteur(mots))

# Exercice 5

def composer(f, g):
    return lambda x: f(g(x))

incremente = lambda x: x + 1
fonction_composée = composer(au_carre, incremente)

print("Résultat de la fonction composée :", fonction_composée(3))

# Exercice 6

def filtrer_et_appliquer(filtre, transformation, liste):
    return [transformation(x) for x in liste if filtre(x)]

mots = ["bonjour", "SaLuT", "banane", ""]
resultat = filtrer_et_appliquer(lambda x: x != "", str.upper, mots)
print(resultat)

# Exercice 7

def memoriser(fonction):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = fonction(n)
        return cache[n]
    return wrapper

@memoriser
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

# Exercice 8

def calculer_remise(prix_list, remise):
    return sum(remise(prix) for prix in prix_list)

produits = [100, 200, 50, 80]
remise_20 = lambda prix: prix * 0.8
prix_apres_remise = calculer_remise(produits, remise_20)

print("Le prix après 20% de remise est :", prix_apres_remise)