import math as m

class vector:
    dir = 0
    mag = 0
    x = 0
    y = 0
    def __init__(self,direccion,magnitud):
        self.dir = direccion
        self.mag = magnitud
        self.x = magnitud * m.cos(m.radians(direccion))
        self.y = magnitud * m.sin(m.radians(direccion))
    def getX (self):
        return self.x
    def getY (self):
        return self.y
    def show (self):
        print("Angulo = ",self.dir)
        print("Magnitud = ",self.mag)
        print("x = ", self.x)
        print("y = ", self.y,"\n")

d1 = float(input("Dame la Angulo del primer vector: "))
m1 = float(input("Dame la Magnitud del primer vector: "))
d2 = float(input("Dame la Angulo del segundo vector: "))
m2 = float(input("Dame la Magnitud del segundo vector: "))

v1 = vector(d1,m1)
v1.show()
v2 = vector(d2,m2)
v2.show()

xr = v1.getX() + v2.getX()
yr = v1.getY() + v2.getY()

mr = m.sqrt((xr**2)+(yr**2))
dr = m.degrees(m.acos(xr/mr))

vr = vector(dr,mr)
vr.show()