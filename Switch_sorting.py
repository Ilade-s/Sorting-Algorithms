"""
First sorting algorithm
The principle will be to iterate the list and switch the element with the next, depending if it's superior or inferior
"""
import copy

def SwitchSort(it, reverse=False):
    """
    Sorting algorithm

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
    for p in range(len(it)*3):
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
    # l = [rnd.randint(0,5) for i in range(4)]
    l = [4,1,3,2]
    print(l)


    lAO = SwitchSort(l)
    print("Asending order :",lAO)

    lDO = SwitchSort(l, True)
    print("Descending order :",lDO)

