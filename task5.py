class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")
        
class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Рисунок ручкой'

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Рисунок карандашом'

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Рисунок маркером'
    
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
