# toate permutarile

def valid():
    return True

def bktrIt(n,m,temp,depth,used):
    global ans
    if depth == 4:
        ans.append(temp[::])
        return
    for i in range(n):
        if not used[i]:
            temp.append(m[i])
            used[i] = True
            # print(temp)
            print(depth)
            bktrIt(n,m,temp,depth+1,used)

            temp.pop()
            used[i] = False

ans = []
# bktrIt(3,[1,2,3],[],1,[False,False,False])

def valid(pos,temp):
    j=1
    for i in reversed(temp):
        if pos==i or pos-j==i or pos+j==i:
            return False
        j+=1
    return True


def nqueens(n, depth,temp):
    global ans
    if depth == n:
        ans.append(temp[::])
    for i in range(1,n+1):
        if valid(i,temp):
            temp.append(i)
            print(temp)
            nqueens(n,depth+1,temp)
            temp.pop()
nqueens(8,0,[])
print(len(ans))

