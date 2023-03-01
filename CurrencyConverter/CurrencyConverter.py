import tkinter as tk
import requests
import json
from PIL import ImageTk, Image
from . import config



class Currency_Converter():
  def __init__(self, master):
    global new_icon
    global new_logo
    self.converter_window = tk.Toplevel(master)
    self.converter_window.geometry('350x300')
    self.converter_window.minsize(350, 300)
    self.converter_window.maxsize(350, 300)
    self.converter_window.title('Currency Converter')
    self.converter_window.iconbitmap('CurrencyConverter/images/CurrencyConverter.ico')

    self.currencies = ['EUR', 'USD', 'JPY', 'GBP','AUD', 'CAD', 'HRK', 'RUB', 'CZK', 'CHF']

    self.first_label = tk.Label(self.converter_window, text='Amount: ', font = ('Arial', 13)).grid(row=1, column=1, columnspan=2)
    
    self.input_entry = tk.Entry(self.converter_window, width= 25)
    self.input_entry.grid(row=2, column=0, columnspan=5)
    
    self.currency_one = tk.StringVar()
    self.currency_two = tk.StringVar()
    
    self.drop = tk.OptionMenu(self.converter_window, self.currency_one, *self.currencies)
    self.drop.grid(row=3, column=1)
    self.drop.config(width=3)
    

    
    #Import the image using PhotoImage function
    click_btn= Image.open('CurrencyConverter/images/rotate.png')
    resized_icon = click_btn.resize((35, 24))
    new_icon = ImageTk.PhotoImage(resized_icon)
    img_label= tk.Label(image=new_icon)


    logo= Image.open('CurrencyConverter/images/CurrencyConverter.png')
    resized_logo = logo.resize((350, 90))
    new_logo = ImageTk.PhotoImage(resized_logo)
    self.logo_label= tk.Label(self.converter_window, image=new_logo)
    self.logo_label.grid(row=0, column=0, columnspan=5)


    self.rotation_button = tk.Button(self.converter_window, image=new_icon, command = self.rotate).grid(row=3, column=2, pady= 15)
    
    self.second_drop = tk.OptionMenu(self.converter_window, self.currency_two, *self.currencies)
    self.second_drop.grid(row=3, column=3)
    self.second_drop.config(width=3)

    self.convert_button = tk.Button(self.converter_window, text='Convert', command=self.Convert, height= 1, width= 20).grid(row=4, column= 0, columnspan=5)

 


  def Convert(self):
      self.final_label = tk.Label(self.converter_window, text='').grid(row=5, column= 0, columnspan=5, pady=10)
      self.first_currency = format(self.currency_one.get())
      self.second_currency = format(self.currency_two.get())
      self.amount = self.input_entry.get()
      url = f"https://api.apilayer.com/currency_data/convert?to={self.second_currency}&from={self.first_currency}&amount={self.amount}"
    
      payload = {}
      headers= {
        "apikey": f"{config.CURRENCY_API_KEY}"
      }
      
      response = requests.request("GET", url, headers=headers, data = payload)
      
      status_code = response.status_code
      result = response.text
      
      self.amount_result = json.loads(result)['result']
      self.final_label = tk.Label(self.converter_window, font = ('Arial', 13), text=f'{self.amount} {self.first_currency} = {self.amount_result} {self.second_currency}')
      self.final_label.grid(row=5, column= 0, columnspan=5, pady=10)
      
        
    
  def rotate(self):
      self.first_currency = format(self.currency_one.get())
      self.second_currency = format(self.currency_two.get())
      self.currency_one.set(self.second_currency)
      self.currency_two.set(self.first_currency)

if __name__ == '__main__':
  monitor = Currency_Converter()
  monitor.mainloop()