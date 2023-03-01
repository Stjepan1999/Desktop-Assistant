import tkinter as tk
from . import frames
from . import widgets
from . import ram_info
from . import disk_info
from . import cpu_info 


class ResourceMonitor():
  def __init__(self, master):
    self.monitor = tk.Toplevel(master)
    self.monitor.title('Resource Monitor')
    self.monitor.iconbitmap("ResourceMonitor/logo/ResourceMonitor.ico")
    self.monitor.geometry('740x430')
    self.monitor.minsize(740, 430)
    self.monitor.maxsize(740, 430)
    self.frames = frames.Frames(self.monitor)
    self.widgets = widgets.Widgets(self.monitor, self.frames.cpu_frame, self.frames.ram_frame, self.frames.disk_frame)

    
    self.cpu_info = cpu_info.Cpu_Info(self.frames.cpu_frame)

    self.ram_info = ram_info.Ram_Info(self.frames.ram_frame)

    self.disk_info = disk_info.Disk_Info(self.frames.disk_frame)
    
    self.monitor.after(1000, self.update_label)




  def update_label(self):
    self.cpu_info = cpu_info.Cpu_Info(self.frames.cpu_frame)

    self.ram_info = ram_info.Ram_Info(self.frames.ram_frame)

    self.monitor.after(1000, self.update_label)

