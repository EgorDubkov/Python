class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h
    def get_size_coat(self):
        return self.v/6.5 + 0.5
    def get_size_jacket(self):
        return self.h*2 + 0.3
    @property
    def get_full(self):
        return str(f'Общее кол-во ткани: {(self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)}')

class Coat(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.size_coat = round(self.v / 6.5 + 0.5)
    def __str__(self):
        return f'Площадь на пальто {self.size_coat}'

class Jacket(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.size_jacket = round(self.h * 2 + 0.3)
    def __str__(self):
        return f'Площадь на жакет {self.size_jacket}'

coat = Coat(5, 5)
jacket = Jacket(3, 3)
print(coat)
print(jacket)
print(coat.get_size_coat())
print(jacket.get_size_jacket())
print(coat.get_full)
print(jacket.get_full)
