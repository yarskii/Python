class Stationery:
    def __init__(self, title):
        self.ti = title

    def draw(self):
        print(f'Запуск отрисовки {self.ti}')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        print(f'Рисунок {self.ti}')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
        print(f'Рисунок {self.ti}')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        print(f'Рисунок {self.ti}')


pen = Pen('ручкой')
pencil = Pencil('карандашом')
handle = Handle('маркером')
pen.draw()
pencil.draw()
handle.draw()
