class Road():
    _length = None
    _width = None
    weigth = None
    thickness = None
    
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        
    def mass(self):
        self.weigth = 25
        self.tickness = 5
        mass = self._length * self._width * self.weigth * self.tickness / 1000
        print(f'{mass}')
        
r = Road(20, 5000)
print(r.mass())
