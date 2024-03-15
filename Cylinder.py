class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def calculate_volume(self):
        return 3.14159265359 * self.radius ** 2 * self.height

    def calculate_base_area(self):
        return 3.14159265359 * self.radius ** 2

    def calculate_lateral_area(self):
        return 2 * 3.14159265359 * self.radius * self.height