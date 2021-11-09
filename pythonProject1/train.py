from transport import *
from random import randint


# Класс, описывающий поезд.
class Train(Transport):
    def __init__(self):
        super().__init__()
        self.number_of_wagons = 0

    # Считываем информацию о поезде из файла.
    def to_transport(self, data_info):
        if len(data_info) != 3:
            return False

        for value in data_info:
            if (not value.isdigit()) or int(value) < 0:
                print("invalid train data")
                return False
        self.speed = int(data_info[0])
        self.the_road = float(data_info[1])
        self.number_of_wagons = int(data_info[2])
        return True

    # Генерируем информацию о поезде.
    def to_rnd_transport(self):
        self.speed = randint(20, 270)
        self.the_road = randint(40, 12000)
        self.number_of_wagons = randint(5, 30)

        return self

    # Выводим информацию о поезде.
    def out_transport(self, output_stream):
        print("TRAIN. Speed: {}, "
              ", distance: {}, "
              ", number of wagons: {}, \n"
              "road time: {:.2f}".format(self.speed, self.the_road,
                                         self.number_of_wagons, self.road_time(), ))
        output_stream.write("TRAIN. Speed: {}, "
                            ", distance: {}, "
                            ", number of wagons: {}, \n"
                            "road time: {:.2f}\n".format(self.speed, self.the_road,
                                                         self.number_of_wagons, self.road_time(), ))
