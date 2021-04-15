import matplotlib.pyplot as plt

listTimeIS = [[],[]]
listTimesort = [[],[]]
listTimeSS = [[],[]]
rlist = [5,500,2000,5000,10000,15000,20000]

listTimeIS[0] = [0.003, 0.218, 0.783, 1.861, 2.92, 5.759, 10.202]
listTimeIS[1] = [0.012, 64.902, 642.989, 2818.485, 10652.621, 24741.013, 48911.853]
listTimeSS[0] =  [0.005, 8.097, 138.013, 792.229, 3269.769, 8257.537, 12960.932]
listTimeSS[1] = [0.271, 6.961, 123.29, 834.456, 3479.22, 7811.064, 16056.485]
listTimesort[0] = [0.004, 0.008, 0.151, 0.058, 0.146, 0.231, 0.172]
listTimesort[1] = [0.002, 0.004, 0.058, 0.058, 0.155, 0.459, 0.333]
listTimeFS = [0.016, 2.707, 15.594, 48.873, 83.356, 119.573, 165.498]

plt.title("Comparaison algorithmes de tri")
# InsertSort()
plt.plot(rlist,listTimeSS[0],"yo-",label="SelectSort() favorable (triée)")
plt.plot(rlist,listTimeSS[1],"mo-",label="SelectSort() défavorable (reversed)")
# SelectSort()
plt.plot(rlist,listTimeIS[0],"ro-",label="InsertSort() favorable (triée)")
plt.plot(rlist,listTimeIS[1],"o-",label="InsertSort() défavorable (reversed)")
# Methode sort()
plt.plot(rlist,listTimesort[0],"go-",label="sorted() favorable (triée)")
plt.plot(rlist,listTimesort[1],"bo-",label="sorted() défavorable (reversed)")
# Tri fusion / fusion sort
plt.plot(rlist,listTimeFS,"co-",label="Tri fusion")

plt.legend()
plt.ylabel("Temps d'exécution (en ms)")
plt.xlabel("Nombre d'éléments (n)")
plt.show()