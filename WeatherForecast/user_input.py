import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
from . import api_call
from . import frames
from . import current_weather
from . import forecast



class User_Input():
    def __init__(self, master_1, master_2, location=None):
        self.master_1 = master_1
        self.master_2 = master_2


        global new_logo
        logo= Image.open('WeatherForecast/icons/WeatherForecast.png')
        resized_logo = logo.resize((380, 90))
        new_logo = ImageTk.PhotoImage(resized_logo)
        self.logo_label= tk.Label(master_1, image=new_logo)
        self.logo_label.grid(row=0, column=0)


        #SQL table for locations
        self.conn = sqlite3.connect('WeatherForecast/Locations.db')
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS locations (city text)')

        #Getting locations from SQL table and putting it to list
        self.locations = []
        self.cur.execute('SELECT city FROM locations')
        for row in self.cur:
            self.locations.append(row[0])
        
        # If the table is empty, initialize it with default location data
        if not self.locations:
            default_locations = ['New York', 'London', 'Paris', 'Tokyo']
            for location in default_locations:
                self.cur.execute(f'INSERT INTO locations (city) VALUES (?)', (location,))
            self.conn.commit()
            self.locations = default_locations

        
        self.location = tk.StringVar()

        #When the program is launched first time it set first location in SQL table, next time it set selected location
        if location == None:
          self.location.set(self.locations[0])
        else:
          self.location.set(location)
        
        
        self.location_optionmenu = tk.OptionMenu(master_2, self.location, *self.locations)
        self.location_optionmenu.place(x=210, y=10)

      
        self.edit_locations_button = tk.Button(master_2, text='Edit Locations', command = self.edit_location).place(x=10, y=10)
        self.show_button = tk.Button(master_2, text='Show', command= lambda:self.get_weather(self.location.get())).place(x=450, y=10)
      
  
    def get_weather(self, location):
        #Refreshing entire program and updating weather info
        self.frames = frames.Frames(self.master_1)
        self.user_input = User_Input(self.master_1, self.frames.input_frame, location)

        self.city = format(self.user_input.location.get())
        self.api_call = api_call.Api_Call(self.city)
      
        self.current_weather = current_weather.Current_Weather(self.frames.current_weather_frame, self.api_call.current_temp, self.api_call.day_1_max_temp, self.api_call.day_1_min_temp, self.api_call.current_condition)
      
        self.forecast = forecast.Forecast(self.frames.forecast_frame, self.api_call.min_max_temp)


    def edit_location(self):
      #Opening new window where user can modify locations
      self.new_window = tk.Toplevel(self.master_1)
      self.new_window.title('Edit locations')
      self.new_window.geometry('400x280')

      input_label = tk.Label(self.new_window, text='Enter the location: ', font=('arial', 12)).place(x=30, y=20)
      self.location_entry = tk.Entry(self.new_window, width=23)
      self.location_entry.place(x=30,y=50)
  
      add_button = tk.Button(self.new_window, text='Add location', font=('arial', 12), width=15, command=self.add_location).place(x=30, y=80)
      
      delete_button = tk.Button(self.new_window, text='Delete', font=('arial', 12), width=15, command=self.delete_location).place(x=30,y=120)
      
      close_button = tk.Button(self.new_window, text='Close', font=('arial', 12), width=15, command=self.exit).place(x=30, y=160)

  
      self.location_listbox = tk.Listbox(self.new_window, height=14, width=30)
      self.location_listbox.place(x=200, y = 20)

      #Inserting current data from SQL to listbox and dropdown menu 
      self.list_update()

      

    def add_location(self):
        #Adding location to SQL table,listbox and dropdown menu, also checking for valid input
        self.city = self.location_entry.get()
        if len(self.city) > 0:
            self.cur.execute('INSERT INTO locations VALUES(:city)',
            {
                'city':self.location_entry.get(),
            })

            self.conn.commit()
            self.location_entry.delete(0, tk.END)
    
        if len(self.city) == 0:
            self.messagebox.showinfo('Empty Entry', 'Enter Location Name')
    
        self.list_update()
    
    def delete_location(self):
        #Deleting location in SQL table,listbox and dropdown menu
        #Can't delete all location because when program is launched for first time need to get location --- this need to be fixed
        selected_location = self.location_listbox.get(self.location_listbox.curselection())
        city = ''
        for item in selected_location:
            city = '' + item
        
        if self.location_listbox.size() > 1:
            self.cur.execute('DELETE FROM locations WHERE city = ?', (city,))
            self.conn.commit()
        if self.location_listbox.size() == 1:
            self.messagebox.showwarning('Warning!', 'Unable to delete all locations')

        self.list_update()

    def exit(self):
        #Exiting from "Edit Location" window
        self.new_window.destroy()

    def list_update(self):
        #Refresing SQL, listbox and optionmenu
        self.locations = []
        self.location_listbox.delete(0, tk.END)
        self.cur.execute('SELECT city FROM locations')
        for row in self.cur:
            self.location_listbox.insert('end', row)
            self.locations.append(row[0])
        self.location_optionmenu = tk.OptionMenu(self.master_2, self.location, *self.locations)
        self.location_optionmenu.place(x=210, y=10)
  
