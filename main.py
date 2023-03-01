import tkinter as tk
from PIL import ImageTk, Image

from CurrencyConverter import CurrencyConverter
from ToDoList import ToDoList
from ResourceMonitor import ResourceMonitor
from WeatherForecast import WeatherForecast



class MainGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        global new_logo
        self.title("Desktop Assistant")
        self.iconbitmap("logo/DesktopAssistantIcon.ico")
        self.geometry("400x470")
        self.minsize(400, 450)
        self.maxsize(400, 450)

        logo= Image.open('logo/DesktopAssistant.png')
        resized_logo = logo.resize((410, 110))
        new_logo = ImageTk.PhotoImage(resized_logo)
        self.logo_label= tk.Label(self, image=new_logo)
        self.logo_label.pack()

        self.create_widgets()

    def create_widgets(self):
        self.weather_button = tk.Button(self, text='Weather Forecast', font=('roboto', 16), command=self.weather_forecast, height=2, width=25)
        self.todolist_button = tk.Button(self, text='To Do List', font=('roboto', 16), command=self.todolist, height=2, width=25)
        self.currency_button = tk.Button(self, text='Currency Converter', font=('roboto', 16), command=self.currency_converter, height=2, width=25)
        self.resourcemonitor_button = tk.Button(self, text='Resource Monitor', font=('roboto', 16), command=self.resource_monitor, height=2, width=25)

        self.weather_button.pack(pady=5)
        self.todolist_button.pack(pady=5)
        self.currency_button.pack(pady=5)
        self.resourcemonitor_button.pack(pady=5)


    def todolist(self):
        try:
            #Checking if there is already open window
            self.todo.deiconify()
            self.todo.focus_force()
        except:
            self.todo = ToDoList.ToDoList(self)

    def currency_converter(self):
        try:
            #Checking if there is already open window
            self.currencyconverter.deiconify()
            self.currencyconverter.focus_force()
        except:
            self.currencyconverter = CurrencyConverter.Currency_Converter(self)
    
    def resource_monitor(self):
        try:
            #Checking if there is already open window
            self.resourcemonitor.deiconify()
            self.resourcemonitor.focus_force()
        except:
            self.resourcemonitor = ResourceMonitor.ResourceMonitor(self)
    
    def weather_forecast(self):
        try:
            #Checking if there is already open window
            self.weatherforecast.deiconify()
            self.weatherforecast.focus_force()
        except:
            self.weatherforecast = WeatherForecast.WeatherForecast(self)


if __name__ == '__main__':
    app = MainGUI()
    app.mainloop()




