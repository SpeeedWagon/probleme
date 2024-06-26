import random
import math
def genMat(n):
    a = []
    for i in range(0,n):
        a.append(random.randint(0,n))
    print(a)
    return a

def partition(a,s,d):
    #  print(s," ",d)
     i = s
     j = d + 1
     pivot = a[s]
     while(True):
          while(True):
            i+=1
            if(i>d or a[i]>=pivot):
                break
          while(True):
            j=j-1
            if(j<s or a[j]<=pivot):
                break
          if i<j:
            aux = a[i]
            a[i] = a[j]
            a[j] = aux
          else:
            aux = a[s]
            a[s] = a[j]
            a[j] = aux
            # print(j)
            return j

def quicksort(a,s,d):
    if s<d:
        ss = partition(a,s,d)
        quicksort(a,s,ss-1)
        quicksort(a,ss+1,d)

m=[10, 12, 3, 9, 15, 8, 2, 19, 16, 4, 6, 13, 5, 20, 11, 1]
quicksort(m,0,15)
print(m)