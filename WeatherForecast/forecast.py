import tkinter as tk
import datetime
from PIL import ImageTk, Image


class Forecast:
  def __init__(self, master, min_max_temp):
    global icons

    #Information about weather, for each day create a dictionary key 'day_<i+1>_data' which stores the data for that specific day.
    self.day_data = {}
    for i in range(5):
        self.day_data[f"day_{i+1}_data"] = min_max_temp[min_max_temp['date'] == min_max_temp['date'].iloc[i]]
        self.day_data[f"day_{i+1}_min_temp"] = self.day_data[f"day_{i+1}_data"]['min_temp'].values[0]
        self.day_data[f"day_{i+1}_max_temp"] = self.day_data[f"day_{i+1}_data"]['max_temp'].values[0]
        self.day_data[f"day_{i+1}_condition"] = self.day_data[f"day_{i+1}_data"]['average_weather_condition'].values[0]


    #Getting name of next 5 days
    self.base = datetime.datetime.today()
    days = [
        (self.base + datetime.timedelta(i)).strftime("%A")
        for i in range(5)
    ]

    #Placing day name, mix and max temp on GUI
    for i, day in enumerate(days):
        tk.Label(master, text = day, font = ('Arial', 11)).grid(row=2, column=i * 2, columnspan=2)
        tk.Label(master, text = f"{self.day_data[f'day_{i+1}_max_temp']}°C").grid(row=0, column=(i * 2) + 1)
        tk.Label(master, text = f"{self.day_data[f'day_{i+1}_min_temp']}°C").grid(row=1, column=(i * 2) + 1)

    #Setting icons for each day through loop
    icons = []
    for i in range(5):
      icon = Image.open(f"WeatherForecast/icons/{self.day_data[f'day_{i+1}_condition']}.png")
      resized_icon = icon.resize((60, 60))
      new_icon = ImageTk.PhotoImage(resized_icon)
      icons.append(new_icon)
      self.icon_label = tk.Label(master, image=new_icon)
      self.icon_label.grid(row=0, column=i*2, rowspan=2)

    



    
    