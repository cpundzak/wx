from cls import setget as s 
def load(d,st):
    masterAr = []
    with open('csv/'+d+'.csv') as f:
        for line in f:
            w = line.split(",")
            masterAr.append(w[0]+","+w[1]+","+w[2]+","+w[3]+","+w[4]+","+w[5]+","+w[6]+","+w[7]+","+w[8]+","+w[9]+","+w[10]+","+w[11])
        for x in range(0, len(masterAr), st):
            line = masterAr[x]
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

