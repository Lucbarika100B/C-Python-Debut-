





listeNonVide = [4,5,6,7,1]

listevide = []

def myRange(borneInf=0,borneSup=0,pas=1,inclureBorne=False):
    listeResultante=[]


    if(borneSup < borneInf):
        if inclureBorne:
            borneSup = borneSup - 1
        val = borneInf
           
        while val > borneSup:
            listeResultante.append(val)
            val = val - pas
    else:
        val=borneInf
        if inclureBorne:
            borneSup = borneSup + 1
        while val<borneSup:
            listeResultante.append(val)
            val = val + pas

    return listeResultante


def retirer (listeOriginale,min,max):
    listeResultante = listeOriginale

    for nombre in range(min,max+1):
        if nombre in listeResultante:
            listeResultante.remove(nombre)


    return listeResultante




