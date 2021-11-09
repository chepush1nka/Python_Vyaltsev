# Класс, описывающий транспортные средства, содердит общие свойства.
class Transport:
    def __init__(self):
        self.speed = 0
        self.the_road = 0

    def to_transport(self, data_info):
        pass

    def to_rnd_transport(self):
        pass

    # Считаем и возвращаем время дороги.
    def road_time(self):
        return self.the_road / self.speed

    def out_transport(self, output_stream):
        pass
