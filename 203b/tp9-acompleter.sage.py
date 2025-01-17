

# This file was *autogenerated* from the file tp9-acompleter.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_5 = Integer(5); _sage_const_7 = Integer(7); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_12 = Integer(12); _sage_const_222763 = Integer(222763); _sage_const_100 = Integer(100); _sage_const_1323269 = Integer(1323269); _sage_const_2886 = Integer(2886)
print("""\
# *************************************************************************** #
# *************************************************************************** #
# TP9 : FACTORISATION DES ENTIERS                                             #
# *************************************************************************** #
# *************************************************************************** #
""")

# CONSIGNES
#
# Les seules lignes a modifier sont annoncee par "Code pour l'exercice"
# indique en commmentaire et son signalees
# Ne changez pas le nom des variables
#
# CONSEILS
#
# Ce modele vous sert a restituer votre travail. Il est deconseille d'ecrire
# une longue suite d'instruction et de debugger ensuite. Il vaut mieux tester
# le code que vous produisez ligne apres ligne, afficher les resultats et
# controler que les objets que vous definissez sont bien ceux que vous attendez.
#
# Vous devez verifier votre code en le testant, y compris par des exemples que
# vous aurez fabrique vous-meme.
#


reset()
print("""\
# ****************************************************************************
# DIVISEURS SUCCESSIFS
# ****************************************************************************
""")


# Donnees de l'enonce de l'exercice

n=_sage_const_2 *_sage_const_3 *_sage_const_3 *_sage_const_5 *_sage_const_5 *_sage_const_5 *_sage_const_7 *_sage_const_11 *_sage_const_11 

# Code pour l'EXERCICE

def div_successives(n):
    return  n.prime_divisors()

# # Affichage des resultats

div_successives(n)
for n in range(_sage_const_2 ,_sage_const_10 ):
    assert(div_successives(ZZ(n))==ZZ(n).prime_divisors())


reset()
print("""\
# ****************************************************************************
# FACTORISATION D'UN NOMBRE B-FRIABLE
# ****************************************************************************
""")


# Donnees de l'enonce de l'exercice

n=_sage_const_2 *_sage_const_3 *_sage_const_3 *_sage_const_5 *_sage_const_5 *_sage_const_5 *_sage_const_7 *_sage_const_11 *_sage_const_11 
P=[p for p in primes(_sage_const_12 )]

# Code pour l'EXERCICE

def div_successives_friable(n, P):
    return  n.prime_divisors()

# # Affichage des resultats

div_successives_friable(n,P)
for n in range(_sage_const_2 ,_sage_const_10 ):
    assert(div_successives_friable(ZZ(n),P)==ZZ(n).prime_divisors())


reset()
print("""\
# ****************************************************************************
# RHO DE POLLARD
# ****************************************************************************
""")


# Donnees de l'enonce de l'exercice

n=_sage_const_222763 

# Code pour l'EXERCICE

def myPollardrho(n):
    x0=Integers(n).random_element()
    return True

# # Affichage des resultats

myPollardrho(n)

for _ in range(_sage_const_5 ):
    n=ZZ.random_element(_sage_const_3 ,_sage_const_100 )
    print(n, 
      "| Resultat rho de Pollard : ", 
      myPollardrho(n), 
      " | n est-il composé ?",not n.is_prime())




reset()
print("""\
# ****************************************************************************
# P-1 DE POLLARD
# ****************************************************************************
""")


# Donnees de l'enonce de l'exercice

n=_sage_const_1323269 

# Code pour l'EXERCICE

def myPollardpm1(n):
    return True


# # Affichage des resultats

myPollardpm1(n)

for _ in range(_sage_const_5 ):
    n=ZZ.random_element(_sage_const_3 ,_sage_const_100 )
    print(n, 
      "| Resultat rho de Pollard : ", 
      myPollardpm1(n), 
      " | n est-il composé ?",not n.is_prime())




reset()
print("""\
# ****************************************************************************
# CRIBLE QUADRATIQUE
# ****************************************************************************
""")


# Donnees de l'enonce de l'exercice

n=_sage_const_2886 

# Code pour l'EXERCICE

def cribleQuadratique (n):
    return  n

# # Affichage des resultats

cribleQuadratique (n)




