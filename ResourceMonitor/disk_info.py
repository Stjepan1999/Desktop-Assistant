import tkinter as tk
import psutil


class Disk_Info:

  def __init__(self, master):
    self.partition = '/'
    self.usage = psutil.disk_usage(self.partition)

    #Summing storage information because psutil library don't have method to sum all partitions
    #Getting information about each partition
    self.total_storage = 0
    self.total_used_storage = 0
    self.total_free_storage = 0
    self.partitions = psutil.disk_partitions()
    for partition in self.partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        storage_gb = round(usage.total/(1024**3), 2)
        used_storage_gb = round(usage.used/(1024**3), 2)
        free_storage_gb = round(usage.free/(1024**3), 2)
        self.total_storage += storage_gb
        self.total_used_storage += used_storage_gb
        self.total_free_storage += free_storage_gb
        self.percentage_used_gb = round(((self.total_used_storage/self.total_storage)*100), 2)
        self.percentage_free_gb = round(100-self.percentage_used_gb, 2)
    

    self.disk_info_widgets(master)

  def disk_info_widgets(self, master):
    self.disk_usage_widget = tk.Label(master, text= f"{round(self.total_storage, 2)}GB").grid(row=1, column=1)

    self.disk_used_widget = tk.Label(master, text= f"{round(self.total_used_storage, 2)}GB ({self.percentage_used_gb}%)").grid(row=2, column=1)

    self.disk_free_widget = tk.Label(master, text= f"{round(self.total_free_storage, 2)}GB ({self.percentage_free_gb}%)").grid(row=3, column=1)

    self.partition_num = tk.Label(master, text = f"{len(self.partitions)}").grid(row=4, column=1)

    for partition in self.partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        storage_gb = round(usage.total/(1024**3), 2)
        used_storage_gb = round(usage.used/(1024**3), 2)
        free_storage_gb = round(usage.free/(1024**3), 2)
        percentage_used_gb = usage.percent 
        partition_label = tk.Label(master, text = f"Partition {partition.device}: {used_storage_gb} / {storage_gb} ({percentage_used_gb}%)").grid(columnspan=2)