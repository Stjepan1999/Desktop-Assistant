import tkinter as tk
import psutil
import wmi

class Cpu_Info:
  def __init__(self, master):
    self.c = wmi.WMI()

    #Get number of cores, max clock speed and name
    for processor in self.c.Win32_Processor():
        self.core_count = processor.NumberOfCores
        self.max_freq = processor.MaxClockSpeed/1000
        self.processor_name = processor.Name

    #Get percent of overall usage
    self.cpu_percent = psutil.cpu_percent()
    
    self.cpu_info_widgets(master)
    

  def cpu_info_widgets(self, master):

    self.cpu_name = tk.Label(master, text=self.processor_name, wraplength=230).grid(row=1, columnspan=2)
    
    self.cpu_usage_label = tk.Label(master, text = f"{self.cpu_percent}%").grid(row=2, column=1)
    
    self.core_count_label = tk.Label(master, text = self.core_count).grid(row=3, column=1)

    self.core_frequency = tk.Label(master, text =f"{self.max_freq} GHz").grid(row=4, column=1)

      