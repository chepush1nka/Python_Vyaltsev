from plane import *
from ship import *
from train import *
from random import randint
import sys
import timer


# Оперделяем к какому виду транспорта относится данное стредство.
def which_transport(transport_type):
    if transport_type == 1:
        transport = Plane()
    elif transport_type == 2:
        transport = Ship()
    elif transport_type == 3:
        transport = Train()
    else:
        print("invalid transport data")
        timer.time_print()
        sys.exit(1)
    return transport


# Класс, описывающий контейнер.
class Container:
    def __init__(self):
        self.data = []

    # Заполнений контейнера данными из файла.
    def fill_container(self, input_stream):
        from_file = input_stream.read()
        file_data = from_file.split("\n")
        for data in file_data:
            transport_data = data.split(" ")
            transport = which_transport(int(transport_data[0]))
            flag = transport.to_transport(data.split(" ")[1:])
            if flag:
                self.data.append(transport)
            else:
                print("invalid transport data")
                return False

        return True

    # Заполняем контейнер случайными значениями.
    def random_fill(self, count):
        for i in range(count):
            transport = which_transport(randint(1, 3))
            self.data.append(transport.to_rnd_transport())

    # Выводим информацию о контейнере.
    def out_container(self, output_stream):
        print("There are ", len(self.data), " vehicles in the container.\n")
        output_stream.write("There are " + str(len(self.data)) + " vehicles in the container.\n")
        for i in range(len(self.data)):
            print(i + 1, ":", end=" ")
            self.data[i].out_transport(output_stream)

