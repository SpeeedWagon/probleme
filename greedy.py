def bulbs(arr):
    cost = 0
    for i in arr:
        if i == 1 and cost % 2 ==0:continue
        if i==0 and cost % 2 == 1:continue
        if i == 1 and cost % 2 == 1:
            cost+=1
        if i == 0 and cost % 2 == 0:cost+=1
    return cost
# print(bulbs([0,1,0,1,0,0,0,1,1,1,1]))
def partition(a,s,d):
    i = s
    j = d + 1
    pivot = a[s]
    while(True):
        while(True):
            i+=1
            if(i>d or a[i]>pivot):
                break
        while(True):
            j = j-1
            if(j<s or a[j]<pivot):
                break
        if i<j:
            aux = a[s]
            a[s] = a[j]
            a[j] = aux
        else:
            aux = a[s]
            a[s] = a[j]
            a[j] = aux
            return j

def quicksort(a,s,d):
    if s<d:
        ss = partition(a,s,d)
        quicksort(a,s,ss-1)
        quicksort(a,ss+1,d)

def highestProduct(arr):
    quicksort(arr,0,len(arr))
    p1 = arr[-1] * arr[-2]*arr[-3]
    p2 = arr[0] * arr [1] * arr[-1]
    return max(p1,p2)

def quicksort2(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x[1] < pivot[1]]
        right = [x for x in arr[1:] if x[1]>= pivot[1]]
        return quicksort2(left) + [arr[0]] + quicksort2(right)
    

def disjointIntervals(arr):
    quicksort2(arr)
    count = 0
    start = arr[0][0]
    end = arr[0][1]
    for i in range(len(arr)-1):
        if(arr[i][1]<arr[i+1][0]): end = arr[i+1][1]
    return end-start

def bani(n):
    bancnote = [1,5,10,25]
    bancnote.reverse()
    sum = 0
    for i in bancnote:
        bnk = n // i
        sum += bnk
        n = n-bnk*i
    return sum
 

