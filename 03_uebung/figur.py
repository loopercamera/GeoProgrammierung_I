import math

class Figur:
    def __init__(self,name):
        self.name = name

    def umfang(self):
        return 0
    
    def __str__(self):
        return self.name
    
class Punkt(Figur):
    def __init__(self,x,y):
        super().__init__("Punkt")
        self.x = x
        self.y = y

class Dreieck(Figur):
    def __init__(self,A,B,C):
        super().__init__("Dreieck")
        self.A = Punkt(A[0], A[1])
        self.B = Punkt(B[0], B[1])
        self.C = Punkt(C[0], C[1])
    

    def umfang(self):
        AB = math.sqrt((self.A.x - self.B.x) ** 2 + (self.A.y - self.B.y) ** 2)
        BC = math.sqrt((self.B.x - self.C.x) ** 2 + (self.B.y - self.C.y) ** 2)
        AC = math.sqrt((self.C.x - self.A.x) ** 2 + (self.C.y - self.A.y) ** 2)
        return AB + BC + AC
    
    def flaeche(self):
        AB = math.sqrt((self.A.x - self.B.x) ** 2 + (self.A.y - self.B.y) ** 2)
        BC = math.sqrt((self.B.x - self.C.x) ** 2 + (self.B.y - self.C.y) ** 2)
        AC = math.sqrt((self.C.x - self.A.x) ** 2 + (self.C.y - self.A.y) ** 2)

        s = (AB + BC + AC)/2
        return math.sqrt(s*(s-AB)*(s-BC)*(s-AC))
        
    
    def __str__(self):
        return f"""
        Ecke 1: ({self.A.x},{self.A.y})
        Ecke 2: ({self.B.x},{self.B.y})
        Ecke 3: ({self.C.x},{self.C.y})"""
    

class Rechteck(Figur):
    def __init__(self,A,C):
        super().__init__("Rechteck")
        self.A = Punkt(A[0],A[1])
        self.C = Punkt(C[0],C[1])

    def umfang(self):
        AB = self.C.x -self.A.x
        BC = self.C.y -self.A.y
        return 2*(AB+BC)
    
    def fleache(self):
        AB = self.C.x -self.A.x
        BC = self.C.y -self.A.y
        return AB * BC
    
    def __str__(self):
        return f"""
        Ecke 1: ({self.A.x},{self.A.y})
        Ecke 2: ({self.C.x},{self.C.y})"""

class Kreis(Figur):
    def __init__(self,mittelpunkt,radius):
        super().__init__("Kreis")
        self.mittelpunkt = Punkt(mittelpunkt[0],mittelpunkt[1])
        self.radius = radius

    def umfang(self):
        return self.radius * math.pi*2
    
    def flaeche(self):
        return self.radius **2 * math.pi
    
    def __str__(self):
        return f"""Mittelpunkt: ({self.mittelpunkt.x},{self.mittelpunkt.y})"""



#class Poloygon(Figur):
 #   def __init__(self,iterativ)





dreieck = Dreieck((1,1),(3,0),(4,1))
print(dreieck.umfang())
print(dreieck.flaeche())
print(dreieck)


rechteck = Rechteck((0,0),(4,2))
print(rechteck.umfang())
print(rechteck)
print(rechteck.fleache())

kreis = Kreis((2,2),2)
print(kreis.umfang())
print(kreis)
print(kreis.flaeche())


