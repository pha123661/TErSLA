
import os


class Config:

    @staticmethod
    def car_speed():
        return 5

    @staticmethod
    def max_fitness():
        return 10000

    @staticmethod
    def angle_clamp():
        return 5

    @staticmethod
    def car_width_base():
        return 15

    @classmethod
    def car_length_base(cls):
        return 2 * cls.car_width_base()

    @classmethod
    def path_width(cls):
        return int(3 * cls.car_width_base())

    @classmethod
    def map_size(cls):
        return cls.map_scaler() * cls.map_base()

    @staticmethod
    def map_scaler():
        return 2

    @classmethod
    def map_base(cls):
        # grid_no = map_base * 2 / 45
        # map_base = grid_no * 45 / 2
        grid_no = 40
        return grid_no * cls.path_width() // cls.map_scaler()

    @staticmethod
    def path_gray_rbg():
        return (180, 255, 35)

    @staticmethod
    def bg_rbg():
        return (27, 70, 24)

    @classmethod
    def grid_size(cls):
        return cls.map_size() // cls.path_width()

    @staticmethod
    def wall_rbg():
        return (64, 64, 64)

    @classmethod
    def used_map_size(cls):
        return cls.path_width() * cls.grid_size()

    @staticmethod
    def result_dir():
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pop50')

    @staticmethod
    def start_pos():
        return (120, 70)
