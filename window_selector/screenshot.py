import tkinter as tk


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.points = []

    def on_click(self, event):
        self.points.append((event.x_root, event.y_root))
        if len(self.points) == 2:
            self.root.quit()  # Hide the main window

    def run(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f'{screen_width}x{screen_height}+0+0')
        self.root.wm_attributes('-alpha', 0.5)
        self.root.bind('<Button-1>', self.on_click)
        self.root.mainloop()
        self.root.destroy()
        return self.points
    