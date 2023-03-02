# **Desktop Assistant**

Desktop Assistant is a Python project that provides a collection of mini apps to help you stay organized and productive on your Windows desktop. Assistant can help you with various tasks, including weather forecast, resource monitoring, currency conversion, and to-do list management. The project is built using Python 3 and the Tkinter library for the GUI.


![Dekstop Assistant GUI](https://i.imgur.com/qy29nsf.png)

# **Features**

## Weather Forecast
The Weather Forecast app provides current weather conditions and a 5-day weather forecast for a given location. It utilizes the OpenWeatherMap API to retrieve weather data.

![Weather Forecast GUI](https://i.imgur.com/pFw52Sh.png)

## Resource Monitor
The Resource Monitor app provides real-time information about system resources, including CPU usage, memory usage, and disk space. It uses the psutil library to access system statistics.

![Resource Monitor GUI](https://i.imgur.com/7W8BG7g.png)

## Currency Converter
The Currency Converter app allows users to convert between different currencies. It uses the APILayer API to retrieve exchange rates.

![Currency Converter GUI](https://i.imgur.com/eRFzhO4.png)

## To-Do List
The To-Do List app allows users to create and manage a list of tasks. Tasks can be added, edited and deleted.

![To Do List GUI](https://i.imgur.com/d9Jg45l.png)


# **Requirements**
To run Desktop Assistant on your Windows PC, you will need to have the following software installed:

•	Python 3.x (available at https://www.python.org/downloads/)

•	The following Python libraries, which can be installed using pip:
-	requests
-	psutil
-	Pillow
-	pandas
-	wmi

Note that Desktop Assistant has only been tested on Windows, and may not work correctly on other operating systems.

# **Getting Started**
To get started with Desktop Assistant, follow these steps:

1.	Clone the repository to your local machine
2.	Install the required dependencies by running `pip install -r requirements.txt`
3.	Edit a config.py files in Weather Forecast and Currency Convertor package to add necessary API keys
4.	Run the main.py script to start the assistant


# **Configuration**
To use the Weather Forecast and Currency Converter apps, you will need to obtain API keys from OpenWeatherMap and APILayer. Add these API keys to your config.py file using the following format:

`WEATHER_API_KEY = 'your_api_key_here'`

`CURRENCY_API_KEY = 'your_api_key_here'`

Links to subscribe to API keys:

- OpenWeatherAPI 5 Days/3 Hour Forecast - https://openweathermap.org/api

- APILayer Currency Converter - https://apilayer.com/marketplace/currency_data-api





# **Contributing**
Contributions to Desktop Assistant are welcome! If you'd like to contribute, please follow these steps:

- Fork the repository
- Create a new branch for your feature or bug fix
- Make your changes and commit them
- Push your changes to your forked repository
- Submit a pull request to the main repository

# **License**
Desktop Assistant is licensed under the MIT License. See the LICENSE file for more information.


