def SelectSort(l):
    """
    entree :
    --------
    tableau : liste d’entier ou réel
            liste à trier

    Sortie :
    --------
    tableau : liste triée
            Attention la liste initiale est modifiée.

    """
    n = len(l)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if l[j] < l[min]: min = j
        tmp = l[i]
        l[i] = l[min]
        l[min] = tmp
    return l


if __name__=='__main__': # test
    import random as rnd

    r = 10
    l = [rnd.randint(0,10) for i in range(10)]
    print(l)
    sl = SelectSort(l)
    print(sl)