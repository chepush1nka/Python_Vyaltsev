from transport import *
from random import randint


# Класс, описывающий самолет.
class Plane(Transport):
    def __init__(self):
        super().__init__()
        self.flight_range = 0
        self.load_capacity = 0

    # Считываем данные о самолете из файла.
    def to_transport(self, data_info):
        if len(data_info) != 4:
            return False
        for value in data_info:
            if not value.isdigit() or int(value) <= 0:
                print("invalid plane data")
                return False
        self.speed = int(data_info[0])
        self.the_road = float(data_info[1])
        self.flight_range = int(data_info[2])
        self.load_capacity = int(data_info[3])

        return True

    # Генерируем информацию о самолете.
    def to_rnd_transport(self):
        self.speed = randint(100, 400)
        self.the_road = randint(300, 9000)
        self.load_capacity = randint(800, 5000)
        self.flight_range = randint(100, 450)

        return self

    # Выводим информацию о самолете.
    def out_transport(self, output_stream):
        print("PLANE. Speed: {}, "
              ", distance: {}, "
              ", load capacity: {}, "
              ", flight range: {}, \n"
              "road time: {:.2f}".format(self.speed, self.the_road,
                                         self.load_capacity, self.flight_range, self.road_time()))
        output_stream.write("PLANE. Speed: {}, "
                            ", distance: {}, "
                            ", load capacity: {}, "
                            ", flight range: {}, \n"
                            "road time: {:.2f}\n".format(self.speed, self.the_road,
                                                         self.load_capacity, self.flight_range, self.road_time()))
