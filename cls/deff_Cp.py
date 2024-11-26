import glob
import os
from cls import setget as s 
def load(d,st):
    masterAr = []
    temp = ""
    with open('csv/'+d+'.csv') as f:
        for line in f:
            masterAr.append(line)
    for q in range(0,len(masterAr),st):
        temp = masterAr[q]
        w = temp.split("[")
        t = w[0].split(" ")
        cdate = t[0]
        ctime = t [1]               
        v = s.wSetGet(cdate,ctime,w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8],w[9],w[10],w[11])
    return v
def loadTodayRain(wx1):
    a = 0
    for x in range(0,wx1.getLen()):
        a = a + wx1.getTodayRain(x)
    return a
def todaysRain(w):
    t = []
    for x in range(0,w.getLen()):
        tr = w.getTodayRain(x)
        t.append(tr)
    s = list((set(t)))
    tr = s
    r = str(tr).split(",")
    tr = r[0]
    tr = tr[2:]
    print(format(float(tr), '.2f'))
def todaysHumidty(w):
    w.resetA()
    temp = ""
    for x in range(0,w.getLen()):
        temp = w.getHum(x)
        r = temp.split(",")
        w.setA(r[0])
    d = max(w.getA())
    print(format(float(d), '.1f'))

def autoLoad(st):
    os.chdir("csv")
    masterAr = []
    q = 0
    for file in glob.glob("*.csv"):
        pass
    return None

def fil(a):
    r = a.split(",")
    return format(float(r[0]), '.1f')

def getMax(wx1):
    a = []
    for x in range(0,wx1.getLen()):
        a.append(wx1.getOutTemp(x))
    return fil(max(a))

def getMin(wx1):
    a = []
    for x in range(0,wx1.getLen()):
        a.append(wx1.getOutTemp(x))
    return fil(min(a))

def getMaxIndex(wx1):
    a = []
    for x in range(0,wx1.getLen()):
        a.append(wx1.getOutTemp(x))
    return a.index(str(max(a)))


    