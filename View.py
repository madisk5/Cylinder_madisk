from tkinter import *
from tkinter import messagebox

class CylinderView(Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title('Silindri kalkulaator')

        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        (self.entry_radius, self.entry_height, self.btn_calculate, self.text_box) = self.create_frame_widgets()

        self.bind('<Return>', lambda event: self.controller.calculate_button_pressed())
        self.bind('<Escape>', self.on_close)
        self.protocol('WM_DELETE_WINDOW', self.on_close)

        self.center_window()
        self.resizable(False, False)

    def center_window(self):
        self.update_idletasks()
        width = 500
        height = 300
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_top_frame(self):
        frame_height = 50

        frame = Frame(self, bg='blanchedalmond', height=frame_height)
        frame.pack(side=TOP, fill=X, expand=True)
        return frame

    def create_bottom_frame(self):
        frame_height = 100

        frame = Frame(self, bg='blanchedalmond', height=frame_height)
        frame.pack(side=TOP, fill=BOTH, expand=True)
        return frame

    def create_frame_widgets(self):
        label_radius = Label(self.top_frame, text="Silindri raadius", font=('Verdana', 12), bg='blanchedalmond')
        label_radius.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        entry_radius = Entry(self.top_frame, font=('Verdana', 12))
        entry_radius.grid(row=0, column=1, padx=5, pady=5)

        label_height = Label(self.top_frame, text="Silindri kõrgus", font=('Verdana', 12), bg='blanchedalmond')
        label_height.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        entry_height = Entry(self.top_frame, font=('Verdana', 12))
        entry_height.grid(row=1, column=1, padx=5, pady=5)

        btn_calculate = Button(self.top_frame, text='Arvuta', font=('Verdana', 12),
                               command=self.controller.calculate_button_pressed)
        btn_calculate.grid(row=1, column=2, rowspan=2, padx=5, pady=5, sticky='ew')

        text_box = Text(self.bottom_frame, font='Verdana', width=50, height=10)
        text_box.pack(expand=True, fill=BOTH, padx=5, pady=5)

        return entry_radius, entry_height, btn_calculate, text_box

    def display_results(self, volume, base_area, lateral_area, radius, height):
        results_text = f'Algandmed:\n'
        results_text += f'Silindri raadius: {radius}\n'
        results_text += f'Silindri kõrgus: {height}\n\n'
        results_text += f'Tulemused:\n'
        results_text += f'Silindri ruumala: {volume:.4f}\n'
        results_text += f'Silindri põhja pindala: {base_area:.4f}\n'
        results_text += f'Silindri külje pindala: {lateral_area:.4f}\n'

        self.text_box.config(state='normal')
        self.text_box.delete('1.0', 'end')
        self.text_box.insert('insert', results_text + '\n')
        self.text_box.config(state='disabled')

    def on_close(self, event=None):
        if messagebox.askokcancel('Välju rakendusest', 'Kas soovid tõesti rakendusest väljuda?'):
            self.destroy()

    def show_error_message(self, message):
        messagebox.showerror('Viga', message)
