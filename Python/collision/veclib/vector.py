import numpy as np
class Vector2d:
    def __init__(self, arg1, arg2, polar = False):
        if polar:
            mag = arg1
            angle = arg2
            self.x = mag * np.cos(angle)
            self.y = mag * np.sin(angle)
            
        else:
            self.x = arg1
            self.y = arg2
    
    def astuple(self):
        return (self.x, self.y)
    
    def mag(self):
        return (self.x**2 + self.y**2)**0.5
    
    def dir(self):
        angle = np.arcsin(self.y/self.mag())
        if self.x < 0 and self.y > 0:
            return np.pi/2 + angle
        elif self.x < 0 and self.y < 0:
            return angle - np.pi/2
        elif self.x < 0 and self.y == 0:
            return angle + np.pi
        return angle

    def polar(self):
        return (self.mag(), self.dir())
    
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector2d(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y
    
    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            return Vector2d(self.x / other, self.y / other)
        return self.x / other.x + self.y / other.y

    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2d(self.x - other.x, self.y - other.y)
    
    def __lt__(self, other):
        return self.mag() < other.mag()
    def __le__(self, other):
        return self.mag() <= other.mag()
    def __eq__(self, other):
        return self.mag() == other.mag()
    def __ne__(self, other):
        return self.mag() != other.mag()
    def __gt__(self, other):
        return self.mag() > other.mag()
    def __ge__(self, other):
        return self.mag() >= other.mag()

    def __repr__(self):
        return f"<{self.x}, {self.y}> : |{self.mag()}| at {(self.dir() / np.pi) * 180}"


if __name__ == '__main__':
    testv = Vector2d(5, np.pi/6, polar = True)
    print(testv)