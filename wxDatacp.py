from cls import deff_Cp as c

w = c.load("2024-11-10",1)
print(c.getMax(w))
print(c.getMin(w))

c.todaysRain(w)

c.todaysHumidty(w)








'''
for x in range(0,w.getLen()):
    if(w.getPerciseA(x)!= "100.0"):
        if(w.getPerciseA(x) != str(d)):
            b.append(w.getPerciseA(x))
c = min(b)
print(c)



Stake Dinner 

put lines 7 & 8 nto deff.py
https://tempestwx.com/history/83172/day/2024/10/30
'''