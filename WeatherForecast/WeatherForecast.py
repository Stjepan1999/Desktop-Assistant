import tkinter as tk
from . import frames
from . import user_input
from . import current_weather
from . import api_call
from . import forecast




class WeatherForecast():
    def __init__(self, master):
        self.weather_gui = tk.Toplevel(master)
        self.weather_gui.title('Weather Forecast')
        self.weather_gui.iconbitmap("WeatherForecast/icons/Weather.ico")
        self.weather_gui.geometry("500x370")
        self.weather_gui.minsize(500, 370)
        self.weather_gui.maxsize(500, 370)


        self.frames = frames.Frames(self.weather_gui)
        self.user_input = user_input.User_Input(self.weather_gui, self.frames.input_frame)
        
        self.city = format(self.user_input.location.get())
        self.api_call = api_call.Api_Call(self.city)
      
        self.current_weather = current_weather.Current_Weather(self.frames.current_weather_frame, self.api_call.current_temp, self.api_call.day_1_max_temp, self.api_call.day_1_min_temp, self.api_call.current_condition)
      
        self.forecast = forecast.Forecast(self.frames.forecast_frame, self.api_call.min_max_temp)
        
        
