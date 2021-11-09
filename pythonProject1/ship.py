from transport import *
from random import randint


# Класс, описываеющий корабль.
class Ship(Transport):
    def __init__(self):
        super().__init__()
        self.ship_type = 0
        self.water_displacement = 0
    ship_time = {
        1: "liner",
        2: "tugboat",
        3: "tanker"
    }

    # Считываем данные о корабле из файла.
    def to_transport(self, data_info):
        if len(data_info) != 4:
            return False
        for value in data_info:
            if not value.isdigit() or int(value) < 0:
                print("invalid ship data")
                return False
        if 1 > int(data_info[2]) or 3 < int(data_info[2]):
            print("invalid ship data")
            return False
        self.speed = int(data_info[0])
        self.the_road = float(data_info[1])
        self.ship_type = int(data_info[2])
        self.water_displacement = int(data_info[3])
        return True

    # Генерируем информацию о корабле.
    def to_rnd_transport(self):
        self.speed = randint(22, 150)
        self.the_road = randint(200, 19000)
        self.ship_type = randint(1, 3)
        self.water_displacement = randint(20000, 50000)

        return self

    # Выводим информацию о корабле.
    def out_transport(self, output_stream):

        print("SHIP. Speed: {}, "
              ", distance: {}, "
              ", ship type: {},"
              ", water_displacement: {}, \n"
              "road time: {:.2f}".format(self.speed, self.the_road,
                                         Ship.ship_time[self.ship_type],
                                         self.water_displacement, self.road_time()))
        output_stream.write("SHIP. Speed: {}, "
                            ", distance: {}, "
                            ", ship type: {},"
                            ", water_displacement: {}, \n"
                            "road time: {:.2f}\n".format(self.speed, self.the_road,
                                                         Ship.ship_time[self.ship_type],
                                                         self.water_displacement, self.road_time()))
