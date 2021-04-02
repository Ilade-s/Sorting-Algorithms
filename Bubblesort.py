"""
First sorting algorithm
The principle will be to iterate the list and Bubble the element with the next, depending if it's superior or inferior
"""
import timeit

l = []
def BubbleSort(it=l, reverse=False):
    """
    Sorting algorithm of Bubble Sort type

    COMPLEXITY :
    ------------
    High/Very Bad or Average : iterate the list (n operation) completely n times

    O(n*n) = O(n^2) ou O(n(n-1)/4)

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
    it = l
    for p in range(len(it)):
        mp = 0
        for i in range(len(it)-p):
            if i<=len(it)-2:
                if it[i]>it[i+1]:
                    mp += 1
                    ii = it[i]
                    it[i] = it[i+1]
                    it[i+1] = ii
        # Optimisation
        if mp==0: 
            if reverse:
                it.reverse()
            return it
        elif mp==(len(it)-2): 
            if not reverse:
                it.reverse()
            return it

# Test fonction
if __name__=="__main__": 
    import random as rnd
    from time import perf_counter_ns
    """
    # random list of len(4)
    l = [rnd.randint(0,200) for i in range(200)]
    # l = [4,1,3,2]
    print(l)
    print("Time passed :",round(timeit.timeit(BubbleSort, number=1), 5))

    lAO = BubbleSort(l)
    print("Asending order :",lAO)

    #lDO = BubbleSort(l, True)
    #print("Descending order :",lDO)
    """
    listTimeBS = [[],[]]
    rlist = [5,500,2000,5000,10000,15000,20000]

    for r in rlist: # + favorable
        l = list(range(r))
        start = perf_counter_ns()
        BubbleSort(l)
        end = perf_counter_ns()
        execution_time = round((end - start)*10**(-6),3)
        listTimeBS[0].append(execution_time)
        #print("Time passed :",listTimeBS[0][rlist.index(r)])

    for r in rlist: # - favorable
        l = list(range(r))
        l.reverse()
        start = perf_counter_ns()
        BubbleSort(l)
        end = perf_counter_ns()
        execution_time = round((end - start)*10**(-6),3)
        listTimeBS[1].append(execution_time)
        #print("Time passed :",listTimeBS[1][rlist.index(r)])
    
    print("+ favorable BubbleSort() (en ms) :",listTimeBS[0])
    print("- favorable BubbleSort() (en ms) :",listTimeBS[1])
