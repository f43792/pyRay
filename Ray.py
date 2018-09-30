from Vec3 import vec3

class ray:
    def __init__(self, a, b):
        self.set_a(a)
        self.set_b(b)

    def set_a(self, value_a):
        if isinstance(value_a, vec3):
            self.__a = value_a
        else:
            raise ValueError('Value must be a Vec3 type.')
    def get_a(self):
        return self.__a

    def set_b(self, value_b):
        if isinstance(value_b, vec3):
            self.__b = value_b
        else:
            raise ValueError('Value must be a Vec3 type.')
    def get_b(self):
        return self.__b

    def point_at_parameter(self, t):
        return (self.a + (t * self.b))

    a = property(get_a, set_a)
    b = property(get_b, set_b)
    origin = property(get_a)
    direction = property(get_b)
    # point_at_parameter = property(get_point_at_parameter)