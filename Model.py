class CylinderModel:
    def __init__(self):
        self.radius = 0
        self.height = 0
        self.volume = 0
        self.base_area = 0
        self.lateral_area = 0

    def set_dimensions(self, radius, height):
        self.radius = radius
        self.height = height

    def calculate_cylinder_properties(self):
        self.volume = self.calculate_volume()
        self.base_area = self.calculate_base_area()
        self.lateral_area = self.calculate_lateral_area()

        return self.volume, self.base_area, self.lateral_area

    def calculate_volume(self):
        return 3.14159265359 * self.radius ** 2 * self.height

    def calculate_base_area(self):
        return 3.14159265359 * self.radius ** 2

    def calculate_lateral_area(self):
        return 2 * 3.14159265359 * self.radius * self.height
