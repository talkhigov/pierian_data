class Line():

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        # формула вычесления длины отрезка по координатам
        x = (self.coor2[0] - self.coor1[0]) ** 2 + (self.coor2[1] - self.coor1[1]) ** 2
        return x ** 0.5
    
    def slope(self):
        # Вычисление углового коэффициента по двум точкам
        x = (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
        return x

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())