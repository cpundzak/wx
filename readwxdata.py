from cls import setget as s 
with open('csv/'+'2024-11-07.csv') as f:
    for line in f:
        w = line.split(",")
        print(w[0]+" "+w[1]+" "+w[2]+" "+w[3]+" "+w[4]+" "+w[5]+" "+w[6]+" "+w[7]+" "+w[8]+" "+w[9]+" "+w[10]+" "+w[11]+" "+w[12]+" "+w[13]+" "+w[14]+" "+w[15]+" "+w[16]+" "+w[17]+" "+w[18]+" "+w[19]+" "+w[20]+" "+w[22]+" "+w[23]+" "+w[24]+" "+w[25]+" "+w[26]+" "+w[27]+" "+w[28]+" "+w[29]+" "+w[30]+" "+w[31]+" "+w[32]+" "+w[33]+" "+w[33]+" "+w[34]+" "+w[35]+" "+w[36])
        wx1 = s.wSetGet(w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8],w[9],w[10],w[11])

print(wx1.getTime(1))

max_value = wx1.getOutTemp(100)

 
print(max_value)  # Output: 9