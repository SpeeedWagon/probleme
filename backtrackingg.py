def valid(nr):
    sum = 0
    for i in nr:
        sum+=i
    if sum == 11:
        return True
    return False
    
ans = []
def patruCif(arr, depth):
    global ans
    if(depth == 4 and valid(arr)):
         ans.append(arr[::])
         return     
    elif(depth==4):
         return
    for i in range(0,10):
        arr[depth] = i
        patruCif(arr,depth+1)

def valid2(arr):
    sum = 0
    for i in arr:sum+=i
    if sum>=15:
        print(arr)
        return True
    return False

def notaMin(arr, depth):
    if(depth==3):
        return arr
    for i in range(1,11):
        arr[depth] = i
        notaMin(arr,depth+1)
        valid2(arr)
# notaMin([0,0,0],0)

def valid3(arr):
    if arr[0] == 'b' and arr[2]!='e' and arr[3] == 'e':
        print(arr)
        return True
    return False

def cuvinte(arr, depth):
    if depth == 4:
        return arr
    for l in ['a','b','c','d','e']:
        if (arr[depth-1] == 'a' or arr[depth-1]=='e') and (l == 'a' or l=='e'):
            pass
        else:
            arr[depth] = l
            # print(arr)
            # print(arr[depth-1]," ",arr[depth])
            valid3(arr)
            cuvinte(arr,depth+1)

patruCif([0,0,0,0],0)
def check(arr):
    sum = 0
    for i in arr:
        for j in i:
            sum +=j
    return 11==sum/len(arr)
print(check(ans))
