"""
Second sorting algorithm
Principle : https://fr.wikipedia.org/wiki/Tri_fusion
"""
import sys
sys.setrecursionlimit(250000)
from time import perf_counter_ns
from copy import deepcopy

def TriFusion(l, reverse=False):
    """
    Implementation of the "tri fusion" alogorithm
    """
    n = len(l)

    if n<=1: # Si vide ou un seul éléments, alors déjà trié
        return l

    if n>2000: # Pour eviter un stack overflow / Recursion error (augmente un peu la complexité : gestion de liste...)
        listtris = []
        # parties complètes de len = 1000
        for p in range(n//1000):
            i = 1000*p
            listtris.append(fusion(TriFusion(l[i:i+1000]),TriFusion(l[i+1000:1000*(p+1)])))
        if n%1000!=0:
            # partie finale/incomplète (si existante)
            i = (n//1000)*1000
            fl = n-i
            listtris.append(fusion(TriFusion(l[i:i+fl//2]),TriFusion(l[i+fl//2:])))
        #print(listtris)
        while len(listtris)>1:
            for i in range(len(listtris)-1):
                tmp = []
                tmp.append(fusion(listtris[i],listtris[i+1]))
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
    l = TriFusion(l)
    end = perf_counter_ns()
    execution_time = round((end - start)*10**(-6),3)
    print("Time passed (ms) :",execution_time)
    #timeListFS.append(execution_time)
    #print("liste triée :",l)
    print("Tri fait")
    #print(timeListFS)


