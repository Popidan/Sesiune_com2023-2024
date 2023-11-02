import math

class PID(object):
    def __init__(self, KP, KD, KI, xTarget, yTarget, hTarget):
        self.KP = KP
        self.KD = KD
        self.KI = KI
        self.xTarget = xTarget
        self.yTarget = yTarget
        self.hTarget = hTarget
        self.Timp = 0.005
        self.xError = 0
        self.yError = 0
        self.hError = 0
        self.lastXError = 0
        self.lastYError = 0
        self.lastHError = 0
        self.lastTransError = 0
        self.transOut = 0
        self.transOutWheelAngle = 0
        self.hOut = 0
        self.transIntergal = 0
        self.maxPower = 1
    def calcul(self, xPos, yPos, hPos):
        
        self.xError = self.xTarget-xPos
        self.yError = self.yTarget-yPos
        self.hError = self.hTarget-hPos
        self.alpha = 90
        self.transError = math.sqrt(self.xError**2+self.yError**2)
        if self.xError != 0:
            self.alpha = math.degrees(round(math.atan(self.yError/self.xError),7))
        if self.alpha>180:
            self.alpha -= 180
        if self.alpha < 0:
            self.alpha += 180
        if self.xError < 0: 
            self.transError = -self.transError
        elif self.xError == 0 and self.yError<0:
            self.alpha = -90
            self.transError = -self.transError
        
        self.transProportional = self.transError
        self.transIntergal += self.transError * self.Timp
        self.transDerivative = (self.transError-self.lastTransError)/self.Timp
        self.transOut = self.transProportional*self.KP + self.transIntergal*self.KI + self.transDerivative*self.KD
        if self.transOut > self.maxPower: 
            self.transOut = self.maxPower
        elif self.transOut < -self.maxPower:
            self.transOut = -self.maxPower
        
        self.transOutWheelAngle = 90 - self.alpha
