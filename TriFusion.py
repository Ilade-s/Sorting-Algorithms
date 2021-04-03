"""
Second sorting algorithm
Principle : https://fr.wikipedia.org/wiki/Tri_fusion
"""

def TriFusion(l, reverse=False):
    """
    Implementation of the "tri fusion" alogorithm

    COMPLEXITY :
    ------------
    Low/Very Good : O(n log(n))

    PARAMETRES :
    ------------
    - l : list
        - list that needs to be sorted
    - reverse : bool
        - If False, sort in asending order
        - If True, sort in descending order
            - default = False
    
    RETURNS :
    - l : list (same type as l)
        sorted list
    """
    n = len(l)

    if n<=1: 
        return l

    else:
        A = l[:n//2]
        B = l[n//2:]
        print(A)
        print(B)
        # tri sur place
        if len(A)<=1:
            pass
        elif A[0] <= A[1]:
            A = [A[0],A[1]]
        else:
            A = [A[1],A[0]]
        if len(B)<=1:
            pass
        elif B[0] <= B[1]:
            B = [B[0],B[1]]
        else:
            B = [B[1],B[0]]

        return(fusion(A,B,n))

def fusion(A,B,n):

    f = []
    while len(f)<n:
        if A==[] or B==[]:
            if A==[]: 
                f.append(B.pop(0))
            elif B==[]: 
                f.append(A.pop(0))
        else:
            if A[0] <= B[0]:
                f.append(A.pop(0))
            else:
                f.append(B.pop(0))
    
    return f

if __name__=='__main__': # Test
    import random as rnd
    r = 8
    l = [4,1,3,2]
    l = [rnd.randint(0,r) for i in range(r)]
    print(l)
    l = TriFusion(l)
    print("liste triée :",l)


