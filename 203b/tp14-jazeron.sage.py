

# This file was *autogenerated* from the file tp14-jazeron.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1823 = Integer(1823); _sage_const_3 = Integer(3); _sage_const_693 = Integer(693); _sage_const_239 = Integer(239); _sage_const_2 = Integer(2); _sage_const_15 = Integer(15); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_281 = Integer(281); _sage_const_263 = Integer(263); _sage_const_165 = Integer(165); _sage_const_127 = Integer(127); _sage_const_210 = Integer(210); _sage_const_199 = Integer(199); _sage_const_61 = Integer(61); _sage_const_11 = Integer(11); _sage_const_24 = Integer(24); _sage_const_34 = Integer(34); _sage_const_5 = Integer(5); _sage_const_27 = Integer(27); _sage_const_10 = Integer(10); _sage_const_2199023255579 = Integer(2199023255579); _sage_const_1435967701832 = Integer(1435967701832); _sage_const_123951463462 = Integer(123951463462); _sage_const_1129476910351 = Integer(1129476910351); _sage_const_1383670460733 = Integer(1383670460733); _sage_const_4 = Integer(4); _sage_const_439 = Integer(439); _sage_const_237 = Integer(237); _sage_const_136 = Integer(136)
print("""\
# *************************************************************************** #
# *************************************************************************** #
# TP14 : LOG DISCRET ET COUPLAGES                                             #
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
# PAS DE BEBE, PAS DE GEANT
# ****************************************************************************
""")


# Donnees de l'enonce de l'exercice

p1 = _sage_const_1823 
Fp1 = FiniteField(p1)
b1 = Fp1(_sage_const_3 )
x1 = Fp1(_sage_const_693 )

p2 = _sage_const_239 
Fp2 = FiniteField(p2)
b2 = Fp2(_sage_const_2 )
x2 = Fp2(_sage_const_15 )


# Code pour l'EXERCICE

def Shanks(x,b):
    Fp = x.parent()
    p = Fp.cardinality()
    s = ceil(sqrt(p-_sage_const_1 ))
    T = dict()
    for j in range(s) :
        beta = x*b**(-j)
        T[beta] = j
    i = _sage_const_0 
    gamma = Fp(_sage_const_1 )
    bprime = b**s
    while gamma not in T.keys() :
        i+=_sage_const_1 
        gamma = gamma * bprime
    j = T[gamma]
    return i*s + j


# # Affichage des resultats

print("Question 2 : Mon algo donne : ", Shanks(x1,b1), "Sage donne : ", log(x1,b1))
print("Question 2 : Mon algo donne : ", Shanks(x2,b2), "Sage donne : ", log(x2,b2))



reset()
print("""\
# ****************************************************************************
# RHO DE POLLARD
# ****************************************************************************
""")


# Donnees de l'enonce de l'exercice

p= _sage_const_281 
Fp = FiniteField(p)
x1 = Fp(_sage_const_263 ) 
b1 = Fp(_sage_const_239 )
x2 = Fp(_sage_const_165 )
b2 = Fp(_sage_const_127 )
x3 = Fp(_sage_const_210 )
b3 = Fp(_sage_const_199 )


# Code pour l'EXERCICE

def rho(g,b):
    Fp = g.parent()
    p = Fp.cardinality()
    Zn = Zmod(p-_sage_const_1 )
    partition = lambda x : hash(x)%_sage_const_3 
    def phi(w,alpha,beta) :
        if partition(w) == _sage_const_0  :
            return (g*w, alpha, beta+_sage_const_1 )
        elif partition(w) == _sage_const_1  :
            return (w**_sage_const_2 , _sage_const_2 *alpha, _sage_const_2 *beta)
        elif partition(w) == _sage_const_2  :
            return (b*w, alpha+_sage_const_1 , beta)
    alpha, beta = randint(_sage_const_1 ,p), randint(_sage_const_1 ,p)
    x, ax, bx = phi(b**alpha*g**beta, alpha, beta)
    y, ay, by = phi(x,ax,bx)
    while x != y :
        x, ax, bx = phi(x ,ax ,bx)
        y, ay, by = phi(y, ay, by)
        y, ay, by = phi(y, ay, by)
    try :
        return Zn((ax-ay))/Zn((by-bx))
    except ZeroDivisionError :
        return rho(g,b) # on essaie avec des nouveaux a0 et b0

# # Affichage des resultats

print("Le log de x=",x1,"en base",b1,"vaut",rho(x1,b1),".")
print("Le log de x=",x2,"en base",b2,"vaut",rho(x2,b2),".")
print("Le log de x=",x3,"en base",b3,"vaut",rho(x3,b3),".")
reset()
print("""\
# ****************************************************************************
# COUPLAGE
# ****************************************************************************
""")


# Donnees de l'enonce de l'exercice

p = _sage_const_61 
Fp = FiniteField(p)
E = EllipticCurve(Fp,[_sage_const_11 ,_sage_const_0 ])
print("groupe de E=", E.abelian_group()) # pour verifier
S = E(_sage_const_24 ,_sage_const_34 )
T = E(_sage_const_5 ,_sage_const_27 )
r = _sage_const_10 
print("Verification de la r-torsion : r*S =", r*S, "et r*T =", r*T)


# Code pour l'EXERCICE

def myLine(P1,P2,S):
    E=P1.curve()
    K=E.base_field()
    x1=P1[_sage_const_0 ]; y1=P1[_sage_const_1 ]; z1=P1[_sage_const_2 ]
    x2=P2[_sage_const_0 ]; y2=P2[_sage_const_1 ]; z2=P2[_sage_const_2 ]
    xS=S[_sage_const_0 ]; yS=S[_sage_const_1 ]; zS=S[_sage_const_2 ]
    if z1==_sage_const_0  and z2==_sage_const_0 :
        return K(_sage_const_1 )
    elif z1==_sage_const_0 :
        return xS-x2*zS
    elif z2==_sage_const_0 :
        return xS-x1*zS
    elif x1==x2 and y1==-y2:
        return xS-x1*zS
    elif x1==x2:
        a=E.a4()
        lamb=(_sage_const_3 *x1**_sage_const_2 +a)/(_sage_const_2 *y1)
    else:
        lamb=(y1-y2)/(x1-x2)
    return yS-y1*zS - (xS-x1*zS)*lamb
    
def myH(P1,P2,S):
    return myLine(P1,P2,S)/myLine(P1+P2,-P1-P2,S)

def myMiller(r,S,P):
    R = S
    f = _sage_const_1 
    b = r.bits()
    for r in b[-_sage_const_2 ::-_sage_const_1 ] :
        f = f**_sage_const_2  * myH(R,R,P)
        R = _sage_const_2 *R
        if r == _sage_const_1  :
            f = f*myH(R,S,P)
            R = R + S
    return f

def myTatePairing(S,T,r):
    try:
        return myMiller(r,S,T)
    except ZeroDivisionError:
        Q = S.curve().random_point()
        return myTatePairing(S,T + Q, r)/myTatePairing(S,Q, r)


# # Affichage des resultats

print("Calcul du couplage", myTatePairing(S,T,r))


reset()
print("""\
# ****************************************************************************
# ATTAQUE M.O.V.
# ****************************************************************************
""")


# Donnees de l'enonce de l'exercice

p = _sage_const_2199023255579 
Fp = FiniteField(p)
E = EllipticCurve(Fp,[_sage_const_1 ,_sage_const_0 ])
P = E(_sage_const_1435967701832  , _sage_const_123951463462 )
Q = E(_sage_const_1129476910351  , _sage_const_1383670460733 )

# Code pour l'EXERCICE

j = E.j_invariant() # j-invariant a faire calculer par une fonction de SageMath
rep2 = f"On a un j-invariant de 1728. On a p!=2 et p = {p%_sage_const_4 } mod 4 donc la courbe est supersinguliere"
r = P.order()
t = GF(r)(p).multiplicative_order()
q = p**t
Fq = FiniteField(q, names=('alpha',)); (alpha,) = Fq._first_ngens(1)
EE = EllipticCurve(Fq,[_sage_const_1 ,_sage_const_0 ])
PP = EE(_sage_const_1435967701832  , _sage_const_123951463462 )
QQ = EE(_sage_const_1129476910351  , _sage_const_1383670460733 )
r = PP.order()
SS = EE.random_point()
while SS.order()!=r or PP.weil_pairing(SS,r) == _sage_const_1  :
    SS = EE.random_point()
zeta1 = PP.weil_pairing(SS,r)
zeta2 = QQ.weil_pairing(SS,r)
lambd = log(zeta2,zeta1)


# # Affichage des resultats

print("p premier ?",p.is_prime())
print("j-invariant de E :",j)
print("p mod 4 =", mod(p,_sage_const_4 ))
print(rep2)
print("Cardinal de E(Fp) :",E.cardinality(),"=",E.cardinality().factor())
print("Ordre de P :",P.order())
print("Cardinal de E(Fq) :",EE.cardinality(),"=",EE.cardinality().factor())
print("Point S :",SS)
print("On calcule zeta1 =",zeta1,", zeta2 =",zeta2,", lambda =",lambd,".")


reset()
print("""\
# ****************************************************************************
# CALCUL D'INDICE
# ****************************************************************************
""")


# Donnees de l'enonce de l'exercice

p = _sage_const_439 
Fp = FiniteField(p)
g = Fp(_sage_const_237 )
b = Fp(_sage_const_136 )
y = _sage_const_11 

# Code pour l'EXERCICE

def facto_friable(x,primes_y):
    fact = factor(x)
    expo = {}
    for pp,exp in fact :
        expo[pp] = exp
    for pp in primes_y :
        expo.setdefault(pp,_sage_const_0 )
    vi = []
    for pp in primes_y :
        vi.append(expo[pp])
    return vi
    
def est_friable(x,primes_y):
    return all([pp in primes_y for (pp,_) in factor(x)])

def LogIndice(g,b,y):
    Fp = g.parent()
    p = Fp.cardinality()
    Zn = Zmod(p-_sage_const_1 )
    primes = Primes()
    q = primes.first()
    primes_y = set()
    while q <= y :
        primes_y.add(q)
        q = primes.next(q)
    
    k = len(primes_y)
    M = (Zn**k).change_ring(ZZ)
    alphas = []
    v = []
    i = _sage_const_1 
    while i <= _sage_const_4 *k :
        alpha = randint(_sage_const_0 ,p-_sage_const_2 )
        gamma = int(b**alpha)
        if est_friable(gamma,primes_y) :
            vi = facto_friable(gamma,primes_y)
            v.append(vi)
            alphas.append(alpha)
            i+=_sage_const_1 
    while M.span(v) != M :
        alphas = []
        v = []
        i = _sage_const_1 
        while i <= _sage_const_4 *k :
            alpha = randint(_sage_const_0 ,p-_sage_const_2 )
            gamma = int(b**alpha)
            if est_friable(gamma,primes_y) :
                vi = facto_friable(gamma,primes_y)
                v.append(vi)
                alphas.append(alpha)
                i+=_sage_const_1 
        
    M = matrix(Zn,v)
    alphas = vector(Zn,alphas)
    logs = M.solve_right(alphas)
    beta = randint(_sage_const_0 ,p-_sage_const_2 )
    while not est_friable(int(b**beta*g),primes_y) :
        beta = randint(_sage_const_0 ,p-_sage_const_2 )
    facto = facto_friable(int(b**beta*g),primes_y)
    return -beta + sum([logs[i]*facto[i] for i in range(k)])

# # Affichage des resultats

print("Le log de g=",g,"en base",b,"vaut",LogIndice(g,b,y),".")
print("Sage donne : ", log(g,b))
