from tkinter import messagebox
from Model import CylinderModel
from View import CylinderView

class CylinderController:
    def __init__(self):
        self.model = CylinderModel()
        self.view = CylinderView(self)

    def run(self):
        self.view.mainloop()

    def calculate_button_pressed(self):
        try:
            radius = float(self.view.entry_radius.get())
            height = float(self.view.entry_height.get())

            if radius <= 0 or height <= 0:
                self.show_error('Silindri raadius ja kõrgus peavad olema positiivsed arvud.')
                return

            self.model.set_dimensions(radius, height)
            volume, base_area, lateral_area = self.model.calculate_cylinder_properties()
            self.view.display_results(volume, base_area, lateral_area, radius, height)

            self.view.entry_radius.delete(0, 'end')
            self.view.entry_height.delete(0, 'end')

            self.view.entry_radius.focus()

        except ValueError:
            self.show_error('Sisestage palun arvulised väärtused kõikidesse väljadesse.')

    def show_error(self, message):
        messagebox.showerror('Viga', message)
