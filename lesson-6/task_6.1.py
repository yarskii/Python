import time


class TrafficLight:

    color = 'Красный', 'Желтый', 'Зеленый'

    def running(self):
        for i in range(len(self.color)):
            print(TrafficLight.color[i])
            if i == 0:
                time.sleep(7)
            elif i == 1:
                time.sleep(2)


a = TrafficLight()
a.running()
