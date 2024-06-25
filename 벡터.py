class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self,other):
        return Vector(self.x - other.x, self.y - other.y)
    def __eq__(self,other):
        return self.x == other.y and self.y == other.y
    def __str__(self):
        return '(%g %g)' %(self.x, self.y)
    
a = Vector(2,3)
b = Vector(2,3)
c = a + b
d = a - b
print(type(c))
print(str(c))
print(str(d))

if a == b: 
    print('동일한 값')