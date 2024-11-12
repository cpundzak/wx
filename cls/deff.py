from cls import setget as s 
def load():
    with open('csv/'+'2024-11-07.csv') as f:
        for line in f:
            w = line.split(",")
            wx1 = s.wSetGet(w[0],fil(w[1]),w[2],w[3],w[4],w[5],w[6],w[7],w[8],w[9],w[10],w[11])
    return wx1

def fil(a):
    w = a[1:]
    t = w 
    return t

def getMax(wx1):
    a = []
    for x in range(0,wx1.getLen()):
        a.append(wx1.getOutTemp(x))
    return max(a)

def getMin(wx1):
    a = []
    for x in range(0,wx1.getLen()):
        a.append(wx1.getOutTemp(x))
    return min(a)

