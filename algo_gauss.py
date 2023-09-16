#dimensions
n = int(input("n:"))
p = int(input("p:")) # ne rien écrire pour ne pas afficher les étapes
if not p >= n:
    raise TypeError("BRO GAUSS T'EMMERDE1")
pr = bool(input("Print ?:"))

def Affiche(m):
    for i in m:
        print(i)
    print()
def makefrac(x):
    if x == int(x):
        return x
    p,d,q,z=0,0,1,x
    while abs(p/q-x)>1e-6:
        z=1/(z%1)
        d,q=q,q*int(z)+d
        p=round(x*q,0)
    return "{}/{}".format(int(p),q) if q != 1 else p
def Sum(l1,l2):
    new = []
    for i in range(len(l1)):
        new += [l1[i]+l2[i]]
    return new
def Mult(l, c):
    new = []
    for i in range(len(l)):
        new += [l[i]*c]
    return new
def Eliminer(l,i):
    coef = - pmmatrice[l][i]/pmmatrice[r][i]
    # print(Mult(pmmatrice[r],coef))
    # print(Sum(pmmatrice[l], Mult(pmmatrice[0],coef)))
    # print(pmmatrice[l])
    cp = Sum(pmmatrice[l], Mult(pmmatrice[r],coef))
    pmmatrice[l] = cp


def Permuter(pmmatrice):
    for i in range(n):
        pmmatrice += [Permutation(i)]


def Verif_el(i,l):
    for x in range(0,i):
        if pmmatrice[l][x] != 0:
            return x
    return -1
def Permutation(i):
    for x in range(len(mmatrice)):
        if mmatrice[x][i] != 0:
            return mmatrice.pop(x)
    return mmatrice.pop(0)

#matrice augmentée
mmatrice = [[0 for _ in range(p+1)] for _ in range(n)]

#coefs
for i in range(n):
    for j in range(p+1):
        mmatrice[i][j] = float(input(f"a({i+1},{j+1})="))

# print(mmatrice)

#permutations
pmmatrice = []
Permuter(pmmatrice)

if pr: Affiche(pmmatrice)

#eliminations
for i in range(n):
    r = Verif_el(i,i)
    while r != -1:
        #eliminer
        #ND I assume that l1 will return True in Verif_el
        Eliminer(i,r)
        if pr : Affiche(pmmatrice)
        if pmmatrice[i][0:p] == [0]*p and pmmatrice[i][-1] != 0:
            print("Le sys n'a pas de solution !")
            exit()
        elif pmmatrice[i][0:p] == [0]*p and pmmatrice[i][-1] == 0:
            print('"solution paramétrique, démerde toi')
            exit()
        mmatrice = pmmatrice
        pmmatrice = []
        Permuter(pmmatrice) #sinon certains système provoquent une division par 0
        r = Verif_el(i,i)

#remontée
# print("remontée avec:\n", pmmatrice)
inconnues = [pmmatrice[-1][-1]/pmmatrice[-1][-2]]
I = 0
for i in range(n-1):
    I += 1
    inc = 0
    for x in range(I):
        inc += pmmatrice[-1-I][-2-x] * inconnues[-1-x]
    inc = - inc + pmmatrice[-1-I][-1]
    feur = pmmatrice[-1-I][-2-I]
    inc = inc / feur
    inconnues = [inc] + inconnues

inco = []
for i in inconnues:
    inco += [makefrac(i)]

print(inco)