import math
base ,exp= 10 , 308

a= base**exp
b = math.pow(base,exp)
print (a-b)

exp += 1

b = math.pow(base,exp)

print(a-b)   
