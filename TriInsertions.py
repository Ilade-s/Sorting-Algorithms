from time import perf_counter_ns # Calcul temps d'exécution
import matplotlib.pyplot as plt # Graphes

def InsertSort(l):
    """
    entree :
    --------
    l : liste d’entier ou réel
            liste à trier

    Sortie :
    --------
    l : liste triée
            Attention la liste initiale est modifiée.
    """
    n = len(l)
    for i in range(n):
        x = l[i]
        j = i
        while j > 0 and l[j-1] > x:
            l[j] = l[j-1]
            j-=1
        l[j] = x

if __name__=='__main__': # test
    listTimeIS = [[],[]]
    listTimesort = [[],[]]
    rlist = [5,500,2000,5000,10000,15000,20000]
    """
    # InsertionSort()
    for r in rlist: # + favorable
        l = list(range(r))
        start = perf_counter_ns()
        sl = InsertSort(l)
        end = perf_counter_ns()
        execution_time = round((end - start)*10**(-6),3)
        listTimeIS[0].append(execution_time)
        print("Time passed :",listTimeIS[0][rlist.index(r)])

    for r in rlist: # - favorable
        l = list(range(r))
        l.reverse()
        start = perf_counter_ns()
        sl = InsertSort(l)
        end = perf_counter_ns()
        execution_time = round((end - start)*10**(-6),3)
        listTimeIS[1].append(execution_time)
        print("Time passed :",listTimeIS[1][rlist.index(r)])
    
    # méthode sort()
    for r in rlist: # + favorable
        l = list(range(r))
        start = perf_counter_ns()
        l.sort()
        end = perf_counter_ns()
        execution_time = round((end - start)*10**(-6),3)
        listTimesort[0].append(execution_time)
        print("Time passed :",listTimesort[0][rlist.index(r)])
    
    for r in rlist: # - favorable
        l = list(range(r))
        l.reverse()
        start = perf_counter_ns()
        l.sort()
        end = perf_counter_ns()
        execution_time = round((end - start)*10**(-6),3)
        listTimesort[1].append(execution_time)
        print("Time passed :",listTimesort[1][rlist.index(r)])
    
    print("+ favorable InsertSort() (en ms) :",listTimeIS[0])
    print("- favorable InsertSort() (en ms) :",listTimeIS[1])
    print("+ favorable sort() (en ms) :",listTimesort[0])
    print("- favorable sort() (en ms) :",listTimesort[1])
    """
    listTimeIS[0] = [0.003, 0.218, 0.783, 1.861, 2.92, 5.759, 10.202]
    listTimeIS[1] = [0.012, 64.902, 642.989, 2818.485, 10652.621, 24741.013, 48911.853]
    listTimesort[0] = [0.004, 0.008, 0.151, 0.058, 0.146, 0.231, 0.172]
    listTimesort[1] = [0.002, 0.004, 0.058, 0.058, 0.155, 0.459, 0.333]

    plt.title("Comparaison InsertSort() et sorted()")
    # InsertSort()
    plt.plot(rlist,listTimeIS[0],"ro-",label="InsertSort() favorable (triée)")
    plt.plot(rlist,listTimeIS[1],"o-",label="InsertSort() défavorable (reversed)")
    # Methode sort()
    plt.plot(rlist,listTimesort[0],"go-",label="sorted() favorable (triée)")
    plt.plot(rlist,listTimesort[1],"bo-",label="sorted() défavorable (reversed)")

    plt.legend()
    plt.ylabel("Temps d'exécution (en ms)")
    plt.xlabel("Nombre d'éléments (n)")
    plt.show()