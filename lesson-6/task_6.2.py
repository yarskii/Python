class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self):
        weight_cons = 25
        thickness = 5
        print(f'{(self._length * self._width * weight_cons * thickness) / 1000} т')


a = Road(20, 5000)
a.weight()
