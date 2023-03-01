import tkinter as tk
import datetime
from PIL import ImageTk, Image


class Current_Weather():
    def __init__(self, master, current_temp, max_temp, min_temp, current_condition):
        global new_icon
        self.master = master
        
        #Date and time
        self.current_condition = current_condition
        self.base = datetime.datetime.today()
        self.today = (self.base + datetime.timedelta(0)).strftime("%A")
        self.timenow = datetime.datetime.now()
        self.current_time = self.timenow.strftime("%H:%M")
        self.time_label = tk.Label(master, text = f"{self.today} {self.current_time}", font = ('Arial', 12))

        #Setting icon for current weather
        icon = Image.open(f'WeatherForecast/icons/{self.current_condition}.png')
        resized_icon = icon.resize((50, 50))
        new_icon = ImageTk.PhotoImage(resized_icon)
        self.icon_label = tk.Label(self.master, image=new_icon)
      
        #Temperature info
        self.current_temp_label = tk.Label(master, text = f"{current_temp}°C", font = ('Arial', 12))
        self.max_temp = tk.Label(master, text= f"{max_temp}°C", font = ('Arial', 12))
        self.min_temp = tk.Label(master, text= f"{min_temp}°C", font = ('Arial', 12))


        #Place geometry
        self.time_label.place(x=200, y=10)
        self.current_temp_label.place(x=240, y=60)
        self.icon_label.place(x=180, y=45)
        self.max_temp.place(x=290, y=40)
        self.min_temp.place(x=290, y=80)


      
