import tkinter as tk



class Frames:
  def __init__(self, master):
    self.master = master
    self.blank_lbl = tk.Label(master, text = '      ').grid(row=1, column=0)


    self.cpu_frame = tk.Frame(master)
    self.cpu_frame.grid(row = 1, column = 1)
    self.cpu_frame.config(highlightbackground="black", highlightthickness=1, width=230, height=300)
    self.cpu_frame.grid_propagate(0)

    self.ram_frame = tk.Frame(master)
    self.ram_frame.grid(row = 1, column = 2)
    self.ram_frame.config(highlightbackground="black", highlightthickness=1, width=230, height=300)
    self.ram_frame.grid_propagate(0)

    self.disk_frame = tk.Frame(master)
    self.disk_frame.grid(row = 1, column = 3)
    self.disk_frame.config(highlightbackground="black", highlightthickness=1, width=230, height=300)
    self.disk_frame.grid_propagate(0)