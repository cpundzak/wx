from cls import deff_Cp as c
w = c.load("2024-10-30",1)
print(c.getMax(w))
print(c.getMin(w))
w.setHighTempIndex(c.getMaxIndex(w))
print(w.getTime(w.getHighTempIndex()))


for x in range(0,w.getLen()):
    w.setTemp(w.getTodayRain(x))
    r = w.getTemp().split(",")
    w.setA(r[0])
d = max(w.getA())


if(len(d) > 0):
    w.setRain(d[0:4])
print(w.getRain())

w.resetA()
temp = ""
for x in range(0,w.getLen()):
    temp = w.getHum(x)
    r = temp.split(",")
    w.setA(r[0])
d = max(w.getA())

b = []
if(len(d) > 0):
    print(d[0:4])

for x in range(0,w.getLen()):
    if(w.getPerciseA(x)!= "100.0"):
        if(w.getPerciseA(x) != str(d)):
            b.append(w.getPerciseA(x))
c = min(b)
print(c)

'''homework, put line(s) 10 - 37 into deff.py def #1 return r def #2 return d def # 2 return  c  def # 2 needs array a as argument
Results are as follows
1.25 for rain
99.0 max hum
67.0 min hum

Stake Dinner 

put lines 7 & 8 nto deff.py
https://tempestwx.com/history/83172/day/2024/10/30
'''