class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} начало движения'

    def stop(self):
        return f'{self.name} конец движения'

    def turn_right(self):
        return f'{self.name} поворот направо'

    def turn_left(self):
        return f'{self.name} поворот налево'

    def show_speed(self):
        return f'Текущая скорость: {self.speed}'
    
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')

        if self.speed > 40:
            return f'Скорость превышена'
        else:
            return f'Скорость в норме'
        
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость машины {self.speed}')

        if self.speed > 60:
            return f'Скорость превышена'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Полицейская'
        else:
            return f'Обычная'
jeegooli = TownCar(40, 'желтая', 'Jeegooli', False)
ferrari = SportCar(120, 'красная', 'Ferrari', False)
mercedes = WorkCar(70, 'белая', 'Mercedes', False)
kia = PoliceCar(80, 'синяя', 'Kia', True)

print(jeegooli.show_speed())
print(ferrari.show_speed())
print(kia.police())
print(mercedes.show_speed())
print(f'{kia.name} {kia.color}')

        
