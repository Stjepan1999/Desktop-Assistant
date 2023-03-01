import tkinter as tk


class Frames:

    def __init__(self, master):
        #Creating three frames
        #First frame is for buttons
        #Second frame is for current temperature information and time information
        #Third frame is for forecast for next 5 days

        self.input_frame = tk.Frame(master)
        self.input_frame.grid(row = 1, column = 0)
        self.input_frame.config(highlightbackground="black", highlightthickness=1, width=500, height=50)
        self.input_frame.grid_propagate(0)


        self.current_weather_frame = tk.Frame(master)
        self.current_weather_frame.grid(row = 2, column = 0)
        self.current_weather_frame.config(width=500, height=120)
        self.current_weather_frame.grid_propagate(0)



        self.forecast_frame = tk.Frame(master)
        self.forecast_frame.grid(row = 3, column = 0)
        self.forecast_frame.config(width=500, height=100)
        self.forecast_frame.grid_propagate(0)