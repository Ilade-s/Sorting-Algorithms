"""
First sorting algorithm
The principle will be to iterate the list and Bubble the element with the next, depending if it's superior or inferior
"""
import copy

def BubbleSort(it, reverse=False):
    """
    Sorting algorithm of Bubble Sort type

    COMPLEXITY :
    ------------
    High/Very Bad : iterate the list (n operation) completely n times

    O(n*n) = O(n^2)

    PARAMETRES :
    ------------
    - it : iterable : list || str
        - iterable that needs to be sorted
    - reverse : bool
        - If False, sort in asending order
        - If True, sort in descending order
            - default = False
    
    RETURNS :
    - it : iterable (same type as it)
        sorted iterable
    """
    for p in range(len(it)):
        for i in range(len(it)):
            iit = copy.deepcopy(it)
            if i<=len(it)-2:
                if it[i]>it[i+1]:
                    iit[i] = it[i+1]
                    iit[i+1] = it[i]
            it = copy.deepcopy(iit)
    if reverse:
        it.reverse()
    
    return it

# Test fonction
if __name__=="__main__": 
    import random as rnd
    # random list of len(4)
    l = [rnd.randint(0,50) for i in range(50)]
    # l = [4,1,3,2]
    print(l)


    lAO = BubbleSort(l)
    print("Asending order :",lAO)

    #lDO = BubbleSort(l, True)
    #print("Descending order :",lDO)

