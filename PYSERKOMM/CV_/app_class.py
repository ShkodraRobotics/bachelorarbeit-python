import tkinter as tk
from tkinter import ttk
import customtkinter as ctk



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")



class conroll_frame(ctk.CTkFrame):
    def __init__(self,container):
        super().__init__(container)

        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=8)

        self.widget()
    def widget(self):
        tabview = ctk.CTkTabview(self)
        tabview.grid(column = 1,row = 0,sticky = ctk.NS)
        tabview.add("tab 1")  # add tab at the end
        tabview.add("tab 2")  # add tab at the end
        tabview.add("tab 3")  # add tab at the end
        tabview.add("tab 4")  # add tab at the end
class app(ctk.CTk):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    def __init__(self):
        super().__init__()

        self.title('RoBo-Vission')
        self.geometry('800x420')
        self.resizable(True,True)

        self.widget()

    def widget(self):
        con_frame = conroll_frame(self)
        con_frame.grid(column = 0,row = 0)





















