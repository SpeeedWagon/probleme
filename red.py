import math as m

def func(x,y,med):
    s = m.pow(med,4)-6*m.pow(med,2) - med + 7
    print(x,y)
    if(abs(s)<=0.003):
        print(med)
        return
    elif(s>0):
        return func(x,(x+y)/2,(x+y)/2)
    elif(s<0):
        return func((x+y)/2,y,(x+y)/2)

def func2(x,y):
    med = (x+y)/2
    s = m.pow(med,4)-6*m.pow(med,2) - med + 7
    while(abs(s)>0.0001):
        med = (x+y)/2
        s = m.pow(med,4)-6*m.pow(med,2) - med + 7
        print(x,y)
        if(s>0):
            y=med
        elif(s<0):
            x=med
func2(2,3)
        