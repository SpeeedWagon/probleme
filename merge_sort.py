import random
import math
def genMat(n):
    a = []
    for i in range(0,n):
        a.append(random.randint(0,n))
    print(a)
    return a

def merge(arr,st,mj,dr):
    i = st
    j = mj+1
    temp = []   
    while i<=mj and j<=dr:
        if arr[i]<arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    while i<=mj:
        temp.append(arr[i])
        i+=1
    while j<=dr:
        temp.append(arr[j])
        j+=1
    print(temp)
    for i in range(0,dr-st+1):
        arr[st+i] = temp[i]

def mergeSort(arr,st,dr):
    if (st < dr) :
        mj = int((dr+st)/2)
        # print(st,' ',mj," ",dr)
        mergeSort(arr,st,mj)
        mergeSort(arr,mj+1,dr)
        merge(arr,st,mj,dr)

m = genMat(16)
mergeSort(m,0,len(m)-1)
# print(m)