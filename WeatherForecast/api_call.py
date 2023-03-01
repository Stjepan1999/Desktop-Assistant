import requests
import pandas as pd
from datetime import datetime
from . import config



class Api_Call():
    def __init__(self, city):
        # Make a request to the OpenWeather API
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={config.WEATHER_API_KEY}&units=metric'
        response = requests.get(url)
        data = response.json()

        self.current_temp = int(data['list'][0]['main']['temp'])
        
        self.current_condition = data['list'][0]['weather'][0]['icon']

        weather_data = []
        # Loop through each item in the list of weather forecasts
        for forecast in data['list']:
            # Get the timestamp of the forecast
            timestamp = forecast['dt']
            # Convert the timestamp to a datetime object
            date = datetime.fromtimestamp(timestamp)
            # Extract the  data from the forecast
            min_temp = forecast['main']['temp_min']
            max_temp = forecast['main']['temp_max']
            weather_condition = forecast['weather'][0]['icon']
            weather_data.append({'date': date, 'min_temp': int(min_temp), 'max_temp': int(max_temp), 'weather_condition': weather_condition})


        weather_df = pd.DataFrame(weather_data)

        # Group the data by date and calculate the average weather condition for each day
        average_weather_condition = weather_df.groupby(weather_df['date'].dt.date)['weather_condition'].agg(lambda x: x.value_counts().index[0]).reset_index()
        average_weather_condition.columns = ['date', 'average_weather_condition']

        # Group the data by date and calculate the min and max temperature for each day
        self.min_max_temp = weather_df.groupby(weather_df['date'].dt.date).agg({'min_temp': 'min', 'max_temp': 'max'}).reset_index()
        self.min_max_temp.columns = ['date', 'min_temp', 'max_temp']
      
        self.day_1_data = self.min_max_temp[self.min_max_temp['date'] == self.min_max_temp['date'].iloc[0]]
        self.day_1_min_temp = self.day_1_data['min_temp'].values[0]
        self.day_1_max_temp = self.day_1_data['max_temp'].values[0]


        # Merge the average_weather_condition DataFrame with the min_max_temp DataFrame
        self.min_max_temp = self.min_max_temp.merge(average_weather_condition, on='date', how='left')



        

