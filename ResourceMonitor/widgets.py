import tkinter as tk
from PIL import ImageTk, Image


class Widgets:

  def __init__(self, master1, master2, master3, master4):
    global new_logo
    self.master = master1

    #Placing logo
    logo= Image.open('ResourceMonitor/logo/ResourceMonitor.png')
    resized_logo = logo.resize((420, 110))
    new_logo = ImageTk.PhotoImage(resized_logo)
    self.logo_label= tk.Label(master1, image=new_logo)
    self.logo_label.grid(row = 0, column = 0, columnspan=4)

    #CPU frame widgets
    self.cpu_frame_label = tk.Label(master2, text= 'CPU', font=('Arial', 16)).grid(row=0, column=0,columnspan=2)
    self.cpu_usage = tk.Label(master2, text='CPU Usage: ').grid(row=2, column=0)
    self.cpu_cores = tk.Label(master2, text='Cores: ').grid(row=3, column=0)
    self.cpu_speed = tk.Label(master2, text = 'CPU Max Speed: ').grid(row=4, column=0)

    #RAM frame widgets
    self.ram_frame_label = tk.Label(master3, text= 'RAM', font=('Arial', 16)).grid(row=0, column=0, columnspan=2)
    self.ram_total_label = tk.Label(master3, text= 'RAM Total: ').grid(row=1, column=0)
    self.ram_used_label = tk.Label(master3, text= 'RAM Used: ').grid(row=2, column=0)
    self.ram_available_label = tk.Label(master3, text= 'RAM Available: ').grid(row=3, column=0)


    #DISK frame widgets
    self.disk_frame_label = tk.Label(master4, text= 'DISK', font=('Arial', 16)).grid(row=0, column=0, columnspan=2)
    self.disk_total = tk.Label(master4, text= 'Total space: ').grid(row=1, column=0)
    self.disk_used = tk.Label(master4, text= 'Used space: ').grid(row=2, column=0)
    self.disk_free = tk.Label(master4, text= 'Free space: ').grid(row=3, column=0)
    self.disk_partitions = tk.Label(master4, text= 'Partitions: ').grid(row=4, column=0)