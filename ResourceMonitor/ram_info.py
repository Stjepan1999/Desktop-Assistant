import tkinter as tk
import psutil


class Ram_Info:

  def __init__(self, master):
    self.mem = psutil.virtual_memory()

    self.ram_total = round(self.mem.total/(1024**3), 2)
    self.ram_used = round(self.mem.used/(1024**3), 2)
    self.ram_used_percent = self.mem.percent
    self.ram_available = round(self.mem.available/(1024**3), 2)
    self.ram_available_percent = 100 - self.mem.percent

    self.ram_info_widgets(master)

  def ram_info_widgets(self, master):
    self.ram_total_widget = tk.Label(master, text = f"{self.ram_total} GB").grid(row=1, column=1)
    
    self.ram_used_widget = tk.Label(master, text = f"{self.ram_used} GB({self.ram_used_percent}%)").grid(row=2, column=1)

    self.ram_available_widget = tk.Label(master, text = f"{self.ram_available} GB({round(self.ram_available_percent, 2)}%)").grid(row=3, column=1)


  

  def update_ram_info(self):
    self.get_ram_info()
    self.ram_info_widgets()
    self.after(1000, self.update_ram_info)
    