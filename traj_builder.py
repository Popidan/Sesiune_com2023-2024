import math

targetPosX = 100
targetPosY = 351
targetPosH = math.radians(375)
if (targetPosX ==0):
    directie_mers = math.radians(90)
else:
    directie_mers = math.atan(targetPosY/targetPosX)

d = math.sqrt(targetPosY**2 + targetPosX**2)
v = 0
vu = 0
heading = math.radians(0)
hError = targetPosH-heading
Vmax = 1

class roata(object):
    def __init__(self, x,y):
        self.xRoata = x
        self.yRoata = y
        self.cRoata = math.atan(self.xRoata/self.yRoata)
        self.aRoata = self.cRoata+hError
        self.r = math.sqrt(self.xRoata**2 + self.yRoata**2)
        self.viteza= 0
        self.b = 0
    def calculStatus(self):
        self.vup = round(math.cos(self.aRoata),7)*vu
        self.vuv = round(math.sin(self.aRoata),7)*vu
        

        if self.vup!=0:
            self.b = round(math.atan((self.vuv+v)/(self.vup)),7)
        else: self.b = math.radians(90)

        
        self.viteza = round(math.sqrt(self.vup**2+(self.vuv+v)**2),7)
        

roata1 = roata(-50,50)
roata2 = roata(50,50)
roata3 = roata(50,-50)
roata4 = roata(-50,-50)

# print(roata3.r*hError)
v = (Vmax*d)/(d+roata1.r*hError)
vu = (Vmax*roata1.r*hError)/(d+roata1.r*hError)
# print(math.degrees(roata1.b))
roata1.calculStatus()
print(round(math.degrees(roata1.b),4), roata1.viteza)
roata2.calculStatus()
print(round(math.degrees(roata2.b),4), roata2.viteza)
roata3.calculStatus()
print(round(math.degrees(roata3.b),4), roata3.viteza)
roata4.calculStatus()
print(round(math.degrees(roata4.b),4), roata4.viteza)


# print(math.degrees(roata3.cRoata), math.degrees(roata3.aRoata))

