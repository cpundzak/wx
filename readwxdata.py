from cls import deff as d
from cls import setget as s
from cls import deff_Cp as c
w = d.load("2024-10-30")
print(d.getMax(w))
print(d.getMin(w))
w.setHighTempIndex(d.getMaxIndex(w))
print(w.getTime(w.getHighTempIndex()))

a = []
temp = ""
for x in range(0,w.getLen()):
    temp = w.getTodayRain(x)
    r = temp.split(",")
    a.append(r[0])
d = max(a)

r = ""
if(len(d) > 0):
    r = d[0:4]
print(r)

a = []
temp = ""
for x in range(0,w.getLen()):
    temp = w.getHum(x)
    r = temp.split(",")
    a.append(r[0])
d = max(a)

b = []
if(len(d) > 0):
    print(d[0:4])

for x in range(0,w.getLen()):
    if(a[x] != "100.0"):
        if(a[x] != str(d)):
            b.append(a[x])
c = min(b)
print(c)

'''homework, put line(s) 10 - 37 into deff.py def #1 return r def #2 return d def # 2 return  c  def # 2 needs array a as argument
Results are as follows
48.4
45.5
0.09
96.0
Stake Dinner 

put lines 7 & 8 nto deff.py
https://tempestwx.com/history/83172/day/2024/10/30
'''