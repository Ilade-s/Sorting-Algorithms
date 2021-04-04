"""
Second sorting algorithm
Principle : https://fr.wikipedia.org/wiki/Tri_fusion
"""
import sys
sys.setrecursionlimit(250000)

def TriFusion(l, reverse=False):
    """
    Implementation of the "tri fusion" alogorithm
    """
    n = len(l)

    if n<=1: # Si vide ou un seul éléments, alors déjà trié
        return l

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
    r = 2000
    #l = [4,1,3,2]
    l = [rnd.randint(0,r) for i in range(r)]
    #print(l)
    l = TriFusion(l)
    #print("liste triée :",l)
    print("Tri fait")


