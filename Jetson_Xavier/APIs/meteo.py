import json
import meteofrance_api as m
from datetime import datetime

data_day = []
data_temperature_min = []
data_temperature_max = []
data_desc = []

dict = {"Jour :": [], "Temperature MIN :": [], "Temperature MAX :": [], "Description :": []}
print("test")
if __name__ == '__main__':
    model = m.MeteoFranceClient()

    forecast = model.get_forecast(48.8534, 2.3488, language='fr').daily_forecast
    jour = 1
    # latitude et longitude de Paris
    
    for day in forecast:
        if jour <= 3:
            data_day.append(datetime.fromtimestamp(day['dt']).isoformat().split('T')[0])
            data_temperature_min.append(day['T']['min'])
            data_temperature_max.append(day['T']['max'])
            if day['weather12H'] is not None:

                desc = day['weather12H']['desc']
                desc = desc.replace('é', 'e')
                desc = desc.replace('è', 'e')
                data_desc.append(desc)
            else:
                data_desc.append(None)
                #m.PictureOfTheDay()
            jour += 1

with open('data_meteo.txt', 'w') as data:
    #on met les données dans un fichier texte data_meteo.txt
    data.write("M-")
    for i in range(len(data_day)):
        data.write(str(data_temperature_min[i]) + "-")
        data.write(str(data_temperature_max[i]) + "-")
        data.write(data_desc[i] + "-")
