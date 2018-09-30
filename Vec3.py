from math import sqrt

class vec3:
    def __init__(self, e0, e1, e2):
        self.set_x(e0)
        self.set_y(e1)
        self.set_z(e2)

    def set_x(self, x):
        self.__e0 = x
            
    def get_x(self):
        return self.__e0

    def set_y(self, y):
        self.__e1 = y
            
    def get_y(self):
        return self.__e1

    def set_z(self, z):
        self.__e2 = z
            
    def get_z(self):
        return self.__e2

    x = property(get_x, set_x)
    r = property(get_x, set_x)

    y = property(get_y, set_y)
    g = property(get_y, set_y)

    z = property(get_z, set_z)
    b = property(get_z, set_z)

    def ifi(self, value):
        """ if is Float or Integer """
        return (type(value) == float or type(value) == int)

    """ operators """
    def __repr__(self):
        return str([i for i in [self.x, self.y, self.z]])

    def __neg__(self):
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z

    def __add__(self, other):
        if isinstance(other, vec3):
            return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __iadd__(self, other):
        if isinstance(other, vec3):
            self.x += other.x
            self.y += other.y
            self.z += other.z

    def __isub__(self, other):
        if isinstance(other, vec3):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z

    def __idiv__(self, other):
        if isinstance(other, vec3):
            self.x /= other.x
            self.y /= other.y
            self.z /= other.z
        if self.ifi(other):
            self.x = self.x / other
            self.y = self.y / other
            self.z = self.z / other

    def __imul__(self, other):
        if isinstance(other, vec3):
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z
        if self.ifi(other):
            self.x = self.x * other
            self.y = self.y * other
            self.z = self.z * other

    def __sub__(self, other):
        if isinstance(other, vec3):
            return vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, vec3):
            return vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        if self.ifi(other):
            return vec3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other):
        if isinstance(other, vec3):
            return vec3(self.x / other.x, self.y / other.y, self.z / other.z)
        if self.ifi(other):
            return vec3(self.x / other, self.y / other, self.z / other)

    def __rmul__(self, other):
        if self.ifi(other):
            return vec3(self.x * other, self.y * other, self.z * other)

    def make_unit_vector(self):
        #k = 1.0 / sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
        k = 1.0 / self.lenght()
        self.x = self.x * k
        self.y = self.y * k
        self.z = self.z * k

    @classmethod
    def dot(cls, va, vb):
        if ((isinstance(va, vec3)) and (isinstance(vb, vec3))):
            return va.x*vb.x + va.y*vb.y + va.z*vb.z

    def squared_lenght(self):
        return ((self.x*self.x) + (self.y*self.y) + (self.z*self.z))

    def lenght(self):
        return sqrt(self.squared_lenght())

    @classmethod
    def unit_vector(cls, va):
        res = va / va.lenght()
        return vec3(res.x, res.y, res.z)