from cls import deff as d
from cls import setget as s

w = d.load("2024-10-31",100)
print(d.getMax(w))
print(d.getMin(w))
w.setHighTempIndex(d.getMaxIndex(w))
print(w.getTime(w.getHighTempIndex()))