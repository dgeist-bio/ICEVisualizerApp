import os
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class ICEVisualizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("KO-Score Visualizer v0.1.0 - Alpha")
        self.geometry("1200x800")

main_app = ICEVisualizerApp()
main_app.mainloop()
