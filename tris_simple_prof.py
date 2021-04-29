
def triSelection(a) :
    n = len(a)
    for i in range(n) :
        min = i
        for j in range(i+1,n) :
            if a[min] > a[j] :
                min = j
        a[min],a[i] = a[i],a[min]

def triInsertion(a) :
    n = len(a)
    for i in range(n) :
        j = i
        while j>0 and a[j-1] > a[j] :
            a[j-1],a[j] = a[j],a[j-1]
            j = j-1


#test du tri pas selection
a=[4,1,3,2]
triSelection(a)
print('tri_selection : ',a)
    
#test du tri par insertion
a=[4,1,3,2]
triInsertion(a)
print('tri_insertion : ',a)

   