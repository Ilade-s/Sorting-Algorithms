"""
Second sorting algorithm
Principle : https://fr.wikipedia.org/wiki/Tri_fusion
"""
from time import perf_counter_ns # mesure du temps d'exécution

def TriFusion(l):
    """
    Implementation of the "tri fusion" algorithm
    """
    n = len(l)

    if n<=1: # Si vide ou un seul éléments, alors déjà trié
        return l
        
    else: 
        sl = []
        A = l[:n//2]
        B = l[n//2:]

        A = TriFusion(A)
        B = TriFusion(B)

        while A!=[] or B!=[]:
            if A==[]:
                sl += B
                break

            elif B==[]:
                sl += A
                break
            
            elif A[0]<=B[0]:
                sl.append(A.pop(0))
            
            elif B[0]<=A[0]:
                sl.append(B.pop(0))
             
        return sl

if __name__=='__main__': # Test
    import random as rnd
    #rlist = [5,500,2000,5000,10000,15000,20000]
    r = int(input("Nombre d'éléments dans la liste : "))
    #r = 20000
    #l = [4,1,3,2]
    #timeListFS = []
    #for r in rlist:
    l = [rnd.randrange(0,r) for i in range(r)]
    #print(l)
    start = perf_counter_ns()
    sl = TriFusion(l)
    end = perf_counter_ns()
    execution_time = round((end - start)*10**(-6),3)
    print("Time passed (ms) :",execution_time)
    if sl == sorted(l):
        print("Tri correct")
    else : 
        print("Tri incorrect")
    #timeListFS.append(execution_time)
    #print("liste triée :",sl)
    #print(len(sl))
    #print("Tri fait")
    #print(timeListFS)


