from time import perf_counter_ns # Calcul temps d'exécution
import matplotlib.pyplot as plt # Graphes

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


if __name__=='__main__': # test
    listTimeSS = [[],[]]
    listTimesort = [[],[]]
    rlist = [5,500,2000,5000,10000,15000,20000]
    """
    # SelectSort()
    for r in rlist: # + favorable
        l = list(range(r))
        start = perf_counter_ns()
        SelectSort(l)
        end = perf_counter_ns()
        execution_time = round((end - start)*10**(-6),3)
        listTimeSS[0].append(execution_time)
        # print("Time passed :",listTime[rlist.index(r)])

    for r in rlist: # - favorable
        l = list(range(r))
        l.reverse()
        start = perf_counter_ns()
        SelectSort(l)
        end = perf_counter_ns()
        execution_time = round((end - start)*10**(-6),3)
        listTimeSS[1].append(execution_time)
        # print("Time passed :",listTime[rlist.index(r)])
    
    # méthode sort()
    for r in rlist: # + favorable
        l = list(range(r))
        start = perf_counter_ns()
        l.sort()
        end = perf_counter_ns()
        execution_time = round((end - start)*10**(-6),3)
        listTimesort[0].append(execution_time)
        # print("Time passed :",listTime[rlist.index(r)])
    
    for r in rlist: # - favorable
        l = list(range(r))
        l.reverse()
        start = perf_counter_ns()
        l.sort()
        end = perf_counter_ns()
        execution_time = round((end - start)*10**(-6),3)
        listTimesort[1].append(execution_time)
        # print("Time passed :",listTime[rlist.index(r)])

    print("+ favorable SelectSort() (en ms) :",listTimeSS[0])
    print("- favorable SelectSort() (en ms) :",listTimeSS[1])
    print("+ favorable sort() (en ms) :",listTimesort[0])
    print("- favorable sort() (en ms) :",listTimesort[1])
    """
    
    listTimeSS[0] =  [0.005, 8.097, 138.013, 792.229, 3269.769, 8257.537, 12960.932]
    listTimeSS[1] = [0.271, 6.961, 123.29, 834.456, 3479.22, 7811.064, 16056.485]
    listTimesort[0] = [0.002, 0.003, 0.011, 0.026, 0.052, 0.088, 0.132]
    listTimesort[1] = [0.001, 0.003, 0.012, 0.027, 0.055, 0.082, 0.114]
    
    plt.title("Comparaison SelectSort() et sorted()")
    # SelectSort()
    plt.plot(rlist,listTimeSS[0],"ro-",label="SelectSort() favorable (triée)")
    plt.plot(rlist,listTimeSS[1],"o-",label="SelectSort() défavorable (reversed)")
    # Methode sort()
    plt.plot(rlist,listTimesort[0],"go-",label="sorted() favorable (triée)")
    plt.plot(rlist,listTimesort[1],"bo-",label="sorted() défavorable (reversed)")

    plt.legend()
    plt.ylabel("Temps d'exécution (en ms)")
    plt.xlabel("Nombre d'éléments (n)")
    plt.show()