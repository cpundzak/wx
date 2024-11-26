from cls import deff_Cp as c

w = c.load("2024-11-10",1)
print(c.getMax(w))
print(c.getMin(w))

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



w.resetA()
temp = ""
for x in range(0,w.getLen()):
    temp = w.getHum(x)
    r = temp.split(",")
    w.setA(r[0])
d = max(w.getA())
print(format(float(d), '.1f'))






'''
for x in range(0,w.getLen()):
    if(w.getPerciseA(x)!= "100.0"):
        if(w.getPerciseA(x) != str(d)):
            b.append(w.getPerciseA(x))
c = min(b)
print(c)

homework, put line(s) 10 - 37 into deff.py def #1 return r def #2 return d def # 2 return  c  def # 2 needs array a as argument
Results are as follows
1.25 for rain
99.0 max hum
67.0 min hum

Stake Dinner 

put lines 7 & 8 nto deff.py
https://tempestwx.com/history/83172/day/2024/10/30
'''