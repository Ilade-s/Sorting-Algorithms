"""
Second sorting algorithm
Principle : https://fr.wikipedia.org/wiki/Tri_fusion
"""
import sys
sys.setrecursionlimit(10**6)
from time import perf_counter_ns
from copy import deepcopy


def TriFusion(l):
    """
    Implementation of the "tri fusion" algorithm
    """
    n = len(l)

    if n<=1: # Si vide ou un seul éléments, alors déjà trié
        return l

    elif n>1000: # Pour eviter un stack overflow / Recursion error (ne corrige rien du tout... casse encore plus vite)
        listtris = []
        # parties complètes de len = 400     
        #print("parts entières :",n//400)
        for p in range(n//400):
            i = p*400
            il = l[i:i+400]
            ilen = len(il)
            listtris.append(fusion(TriFusion(il[:ilen//2]),TriFusion(il[ilen//2:])))
        if n%400!=0:
            # partie finale/incomplète (si existante)
            #print("élements restants :",n-(n//400)*400)
            fl = l[(n//400)*400:]
            flen = len(fl)
            listtris.append(fusion(TriFusion(fl[:flen//2]),TriFusion(fl[flen//2:])))
        #print(listtris)
        while len(listtris)>1:
            #print(len(listtris))
            tmp = []
            for i in range(0,len(listtris),2):
                try:
                    tmp.append(fusion(listtris[i],listtris[i+1]))
                except:
                    tmp.append(listtris[i])
            listtris = deepcopy(tmp)
            

        
        #print(listtris)
        #print(len(listtris))
        return listtris[0]


        

    else: 
        return fusion(TriFusion(l[:n//2]),TriFusion(l[n//2:]))


def fusion(A,B):
    """
    fusionne A et B
    """
    if A==[]:
        return B
    elif B==[]:
        return A
    
    elif A[0]<=B[0]:
        return [A[0]] + fusion(A[1:], B)
    
    elif B[0]<=A[0]:
        return [B[0]] + fusion(A, B[1:])

if __name__=='__main__': # Test
    import random as rnd
    r = int(input("Nombre d'éléments dans la liste : "))
    #r = 20000
    #l = [4,1,3,2]
    #timeListFS = []
    l = [rnd.randint(0,r) for i in range(r)]
    #print(l)
    start = perf_counter_ns()
    sl = TriFusion(l)
    end = perf_counter_ns()
    execution_time = round((end - start)*10**(-6),3)
    print("Time passed (ms) :",execution_time)
    #timeListFS.append(execution_time)
    #print("liste triée :",sl)
    #print(len(sl))
    print("Tri fait")
    if sl == sorted(l):
        print("Tri correct")
    else : 
        print("Tri incorrect")
    #print(timeListFS)


