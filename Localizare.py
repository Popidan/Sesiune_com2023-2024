#prototip localizare
import math
#coordonate roti paralele
pix = 0
piy = 0
pih = 0

xParalele = 0
yParalele1 = 50
yParalele2 = -yParalele1
xPerpendiculara = 40
yPerpendiculara = 0
a1 = math.atan(xParalele/yParalele1)
a2 = math.atan(xParalele/yParalele2)
b = math.atan(yPerpendiculara/xPerpendiculara)
l = math.sqrt(xParalele**2+yParalele1**2)
p3 = math.sqrt(xPerpendiculara**2+yPerpendiculara**2)
razaRoata = 16
numarTickuriPRotatie = 1
c = (2*math.pi*razaRoata)/numarTickuriPRotatie #distanta parcursa per tick
n1 = 23#numar tickuri roata stanga
n2 = 0 #numar tickuri roata dreapta
n3 = 332 #numar tickuri roata fata

dx = c*(n2+n1)/2 #deplasare pe x
dh = (c*(n2-n1)*round(math.cos(a2),7))/(2*l) #diferenta de heading
dy = c*n3-(p3/round(math.cos(b),7))*dh #deplasare pe y

trueX = pix + dx
trueY = piy + dy
trueH = pih + dh
print("x:",trueX)
print("y:",trueY)
print("h:",trueH)
print(c)

