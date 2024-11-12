from cls import setget as s 
from cls import deff as d


with open('csv/'+'2024-11-07.csv') as f:
    for line in f:
        w = line.split(",")
        wx1 = s.wSetGet(w[0],d.fil(w[1]),w[2],w[3],w[4],w[5],w[6],w[7],w[8],w[9],w[10],w[11])
for x in range(0,wx1.getLen()):
    print(wx1.getOutTemp(x))