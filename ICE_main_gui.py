import os
import customtkinter as ctk
from tkinter import filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class ICEVisualizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("KO-Score Visualizer v0.2.0 - Alpha")
        self.geometry("1200x800")

        self.knockout_values = None

        self.knockout_text = ctk.CTkEntry(self, placeholder_text="Please write the first KO-Score!")
        self.knockout_text.pack()

        fastq_file = ctk.CTkButton(self, text="Select File", command=self.load_files)
        fastq_file.pack()

        btn = ctk.CTkButton(self, text="Analysis of Data", command=self.load_knockout_values, corner_radius=2)
        btn.pack()

    def load_knockout_values(self):
        ko_score = self.knockout_text.get()
        corrected_ko_score = float(ko_score)

        print(corrected_ko_score)

    def load_files(self):
        self.selected_file = filedialog.askopenfilename()
        print(self.selected_file)


main_app = ICEVisualizerApp()
main_app.mainloop()
