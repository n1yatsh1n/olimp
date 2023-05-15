f = open('input.txt')
# размеры параллелепипеда
kord = f.readline()
a, b, c = kord.split(' ')
a = int(a)
b = int(b)
c = int(c)

# координаты точек на плоскости параллелепипеда
spider = f.readline().split(' ')
muha = f.readline().split(' ')
Sx = int(spider[0])
Sy = int(spider[1])
Sz = int(spider[2])
Fx = int(muha[0])
Fy = int(muha[1])
Fz = int(muha[2])

r1 = 0
r2 = 0

if (Sx != Fx and (Sx == a or Sx == 0) and (Fx == a or Fx == 0)):
    r1 = min(abs(Sy+Fy), abs((a-Sy)+(a-Fy))) + abs(Sx-Fx)
    r2 = abs(Sz-Fz)
elif (Sy != Fy and (Sy == b or Sy == 0) and (Fy == b or Fy == 0)):
    r1 = min(abs(Sx + Fx), abs((a - Sx) + (a - Fx))) + abs(Sy - Fy)
    r2 = abs(Sz - Fz)
elif (Sz != Fx and (Sz == c or Sz == 0) and (Fz == b or Fz == 0)):
    r1 = min(abs(Sz + Fz), abs((c - Sx) + (c - Fz))) + abs(Sy - Fy)
    r2 = abs(Sx - Fx)
elif ((Sx == 0 or Sx == a) and (Fy == 0 or Fy == b) or (Fx == 0 or Fx == a) and (Sy == 0 or Sy == b)):
    r1 = abs(Sx - Fx) + abs(Sy - Fy)
    r2 = abs(Sz - Fz)
elif ((Sy == 0 or Sy == b) and (Fz == 0 or Fz == c) or (Fy == 0 or Fy == b) and (Sz == 0 or Sz == c)):
    r1 = abs(Sz - Fz) + abs(Sy - Fy)
    r2 = abs(Sx - Fx)
else:
    r1 = abs(Sx-Fx) + abs(Sz - Fz)
    r2 = abs(Sy - Fy)

result = (r1**2 + r2 **2) ** 0.5
print(result)