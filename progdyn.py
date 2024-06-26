def fibDinamic(n):
    arr = []
    arr.append(0)
    arr.append(1)
    for i in range(2,n+1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[-1]

arr = []

def fill(n):
    global arr
    for i in range(0,n):
        arr.append(-1)


def fiboDyn(n):
    global arr
    if arr[n-1] == -1:
        if n == 0 or n == 1:
            arr[n-1] = n
        else:
            arr[n-1] = fiboDyn(n-1) + fiboDyn(n - 2)
    return arr[n-1]
            
def valid(arr):
    sum = 0
    for i in arr:
        sum+=i
    if(sum<=15):
        return True
    return False

ans = []

def backtracking(arr,depth):
    global ans
    if(valid(arr) and depth==4):
        ans.append(arr[::])
        return
    elif(depth==4):
        return
    for i in [0,2,4,5,7,9]:
        if(valid(arr)):
            arr.append(i)
            backtracking(arr,depth+1)
            arr.pop()

