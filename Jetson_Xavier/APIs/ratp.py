import time
import os
import requests, json
import urllib.request
import json


tableau_api_key = ["token_test","414fdd3a-9c28-4280-8c41-397312b92267","7f24ba38-a406-4e60-b5bf-28065ce63590","5286be0d-1a47-449a-bdbe-72a27fc0cda6","31509851-87be-4ad2-b4c9-0ecf93b6cb95","40816be1-7f64-4583-84b8-9101065bb28f","84a456dc-4374-454d-b8e2-a393b800b09f","e3b679ec-443c-4425-a3ec-987abfcd6b71", "a35c9bd4-4d9b-447e-9976-4f2cf605bcc9","c38dbbb9-f93e-4d05-9d16-265403aa6383","274b5318-502a-4f95-9750-07374981606d"]               


# 
# Métro
data_ligne_10 = {"Direction :": [], "Heure de passage = :": []}
data_ligne_7 = {"Direction :": [], "Heure de passage = :": []}

directions_10 = []
directions_7 = []
directions_89 = []
directions_89_2 = []
directions_63 = []
directions_67 = []

horaires_10 = []
horaires_7 = []
horaires_89 = []
horaires_89_2 = []
horaires_63 = []
horaires_67 = []
# Bus
data_bus_89 = {"Direction :": [], "Heure de passage = :": []}     # Arrêt Jussieu : direction Gare de Vanves - Malakoff
data_bus_89_2 = {"Direction :": [], "Heure de passage = :": []}   # Arrêt Cuvier : direction porte de France
data_bus_63 = {"Direction :": [], "Heure de passage = :": []}     # Arrêt Cuvier : directions Porte de la Muette et Gare de Lyon
data_bus_67 = {"Direction :": [], "Heure de passage = :": []}     # Arrêt Jussieu : directions Palais Royal - Musée du Louvre et Stade Charléty - Porte de Gentilly


url_ligne10 = "https://api.navitia.io/v1/coverage/fr-idf/stop_areas/stop_area%3AIDFM%3A71148/lines/line%3AIDFM%3AC01380/departures?count=6&depth=2&"
url_ligne7 = "https://api.navitia.io/v1/coverage/fr-idf/stop_areas/stop_area%3AIDFM%3A71148/lines/line%3AIDFM%3AC01377/departures?count=8&depth=2&"
url_bus89 = "https://api.navitia.io/v1/coverage/fr-idf/stop_areas/stop_area%3AIDFM%3A71148/lines/line%3AIDFM%3AC01121/departures?count=2&depth=2&"
url_bus89_2 = "https://api.navitia.io/v1/coverage/fr-idf/stop_areas/stop_area%3AIDFM%3A71155/lines/line%3AIDFM%3AC01121/departures?count=6&depth=2&"
url_bus63 = "https://api.navitia.io/v1/coverage/fr-idf/stop_areas/stop_area%3AIDFM%3A71155/lines/line%3AIDFM%3AC01099/departures?count=6&depth=2&"
url_bus67 = "https://api.navitia.io/v1/coverage/fr-idf/stop_areas/stop_area%3AIDFM%3A71148/lines/line%3AIDFM%3AC01103/departures?count=6&depth=2&"

#try code 200 ca marche on continue, ca marche pas on incremente la token avec notre tableau de token et on reessaye

for token in tableau_api_key:
    headers = {'Authorization': token}
    response1 = requests.get(url_ligne10, headers=headers)
    if response1.status_code==200 :
        break
    else :
        print(str(token) + "  Cette token est invalide, on en prend un autre")
    
response1 = requests.get(url_ligne10, headers=headers)
response2 = requests.get(url_ligne7, headers=headers)
response3 = requests.get(url_bus89, headers=headers)
response4 = requests.get(url_bus63, headers=headers)
response5 = requests.get(url_bus89_2, headers=headers)
response6 = requests.get(url_bus67, headers=headers)


data_req10 = response1.json()
data_req7 = response2.json()
data_req89 = response3.json()
data_req89_2 = response5.json()
data_req63 = response4.json()
data_req67 = response6.json()


with open("src/data_metro.txt", "w") as data:
    data.write("R ")

dir1_1=0 # villejuif
dir1_2=0 # mairie d'ivry
dir2=0   # La courneuve
#tableau de 4 int dans une variable
attentes = [0,0,0,0,0,0]


# LIGNE 7 #
for departure in data_req7['departures']:
    heure_passage = departure['stop_date_time']['departure_date_time'].split('T')[1]
    heure_passage = heure_passage[:2] + 'h' + heure_passage[2:4] + 'm' + heure_passage[4:6] + 's'
    direction = departure['display_informations']['direction'] 
    #on affiche ensuite la direction
    print('Direction:', direction)

    
    # pattern de prints de debug
    print('Heure de passage:', heure_passage)

    #on recup l'heure + minute actuelle
    heure_actuelle = time.strftime("%H:%M:%S", time.localtime())
    heure_actuelle = heure_actuelle.split(':')
    minute_actuelle = int(heure_actuelle[1])
    heure_actuelle = int(heure_actuelle[0])
    attente = (int(heure_passage[:2]) - heure_actuelle)*60 + int(heure_passage[3:5]) - minute_actuelle

    if direction == "La Courneuve - 8 Mai 1945 (La Courneuve)" and dir1_1 == 0:
        dir1_1=1
        attentes[0] = attente

    elif direction == "Mairie d'Ivry (Ivry-sur-Seine)" and dir1_2 == 0:
        dir1_2 = 1
        attentes[2] = attente
    
    elif direction == "Villejuif - Louis Aragon (Villejuif)" and dir2 == 0:
        attentes[4] = attente
        dir2 = 1

    elif direction == "La Courneuve - 8 Mai 1945 (La Courneuve)" and dir1_1 == 1:
        attentes[1] = attente
        dir1_1=2

    elif direction == "Mairie d'Ivry (Ivry-sur-Seine)" and dir1_2 == 1:
        attentes[3] = attente
        dir1_2 = 2

    elif direction == "Villejuif - Louis Aragon (Villejuif)" and dir2 == 1:
        attentes[5] = attente
        dir2 = 2

        


with open("src/data_metro.txt", "a") as data:
    #on ecrit attente + " "
    data.write(str(attentes[0]) + " ")
    data.write(str(attentes[1]) + " ")
    data.write(str(attentes[2]) + " ")
    data.write(str(attentes[3]) + " ")
    data.write(str(attentes[4]) + " ")
    data.write(str(attentes[5]) + " ")


    
dir1=0
dir2=0
#tableau de 4 int dans une variable
attentes = [0,0,0,0]
# LIGNE 10 #
for departure in data_req10['departures']:
    heure_passage = departure['stop_date_time']['departure_date_time'].split('T')[1]
    heure_passage = heure_passage[:2] + 'h' + heure_passage[2:4] + 'm' + heure_passage[4:6] + 's'
    direction = departure['display_informations']['direction'] 
    #on affiche ensuite la direction
    print('Direction:', direction)

    
    # pattern de prints de debug
    print('Heure de passage:', heure_passage)

    #on recup l'heure + minute actuelle
    heure_actuelle = time.strftime("%H:%M:%S", time.localtime())
    heure_actuelle = heure_actuelle.split(':')
    minute_actuelle = int(heure_actuelle[1])
    heure_actuelle = int(heure_actuelle[0])
    attente = (int(heure_passage[:2]) - heure_actuelle)*60 + int(heure_passage[3:5]) - minute_actuelle

    if direction == "Boulogne Pont de Saint-Cloud (Boulogne-Billancourt)" and dir1 == 0:
        dir1=1
        attentes[0] = attente
    elif direction == "Gare d'Austerlitz (Paris)" and dir2 == 0:
        dir2 = 1
        attentes[2] = attente
    
    elif direction == "Boulogne Pont de Saint-Cloud (Boulogne-Billancourt)" and dir1 == 1:
        attentes[1] = attente
        dir1=2
    
    elif direction == "Gare d'Austerlitz (Paris)" and dir2 == 1:
        attentes[3] = attente
        dir2 = 2


with open("src/data_metro.txt", "a") as data:
    #on ecrit attente + " "
    data.write(str(attentes[0]) + " ")
    data.write(str(attentes[1]) + " ")
    data.write(str(attentes[2]) + " ")
    data.write(str(attentes[3]) + " ")


############################################################### BUSSSSSS ###############################################################
with open("src/data_bus.txt", "w") as data:
    data.write("R ")

dir1=0
attentes = [0,0]
# BUS 89 # ARRET JUSSIEU, DIR : Gare de Vanves - Malakoff
for departure in data_req89['departures']:
    heure_passage = departure['stop_date_time']['departure_date_time'].split('T')[1]
    heure_passage = heure_passage[:2] + 'h' + heure_passage[2:4] + 'm' + heure_passage[4:6] + 's'
    direction = departure['display_informations']['direction'] 
    #on affiche ensuite la direction
    print('Direction:', direction)

    
    # pattern de prints de debug
    print('Heure de passage:', heure_passage)

    #on recup l'heure + minute actuelle
    heure_actuelle = time.strftime("%H:%M:%S", time.localtime())
    heure_actuelle = heure_actuelle.split(':')
    minute_actuelle = int(heure_actuelle[1])
    heure_actuelle = int(heure_actuelle[0])
    attente = (int(heure_passage[:2]) - heure_actuelle)*60 + int(heure_passage[3:5]) - minute_actuelle

    if dir1 == 0:
        dir1=1
        attentes[0] = attente
    
    elif dir1 == 1:
        dir1 = 2
        attentes[1] = attente


with open("src/data_bus.txt", "a") as data:
    #on ecrit attente + " "
    data.write(str(attentes[0]) + " ")
    data.write(str(attentes[1]) + " ")


dir1=0
attentes = [0,0]
# BUS 89 # ARRET JUSSIEU, DIR : Gare de Vanves - Malakoff
for departure in data_req89_2['departures']:
    heure_passage = departure['stop_date_time']['departure_date_time'].split('T')[1]
    heure_passage = heure_passage[:2] + 'h' + heure_passage[2:4] + 'm' + heure_passage[4:6] + 's'
    direction = departure['display_informations']['direction'] 
    #on affiche ensuite la direction
    print('Direction:', direction)

    
    # pattern de prints de debug
    print('Heure de passage:', heure_passage)

    #on recup l'heure + minute actuelle
    heure_actuelle = time.strftime("%H:%M:%S", time.localtime())
    heure_actuelle = heure_actuelle.split(':')
    minute_actuelle = int(heure_actuelle[1])
    heure_actuelle = int(heure_actuelle[0])
    attente = (int(heure_passage[:2]) - heure_actuelle)*60 + int(heure_passage[3:5]) - minute_actuelle

    if dir1 == 0:
        dir1=1
        attentes[0] = attente
    
    elif dir1 == 1:
        dir1 = 2
        attentes[1] = attente


with open("src/data_bus.txt", "a") as data:
    #on ecrit attente + " "
    data.write(str(attentes[0]) + " ")
    data.write(str(attentes[1]) + " ")


dir1=0
dir2=0
attentes = [0,0,0,0]
# BUS 67 Cuvier #
for departure in data_req67['departures']:
    heure_passage = departure['stop_date_time']['departure_date_time'].split('T')[1]
    heure_passage = heure_passage[:2] + 'h' + heure_passage[2:4] + 'm' + heure_passage[4:6] + 's'
    direction = departure['display_informations']['direction'] 
    #on affiche ensuite la direction
    print('Direction:', direction)

    
    # pattern de prints de debug
    print('Heure de passage:', heure_passage)

    #on recup l'heure + minute actuelle
    heure_actuelle = time.strftime("%H:%M:%S", time.localtime())
    heure_actuelle = heure_actuelle.split(':')
    minute_actuelle = int(heure_actuelle[1])
    heure_actuelle = int(heure_actuelle[0])
    attente = (int(heure_passage[:2]) - heure_actuelle)*60 + int(heure_passage[3:5]) - minute_actuelle

    if direction == "Stade Charléty - Porte de Gentilly (Paris)" and dir1 == 0:
        dir1=1
        attentes[0] = attente
    elif direction == "Palais Royal - Musée du Louvre (Paris)" and dir2 == 0:
        dir2 = 1
        attentes[2] = attente
    
    elif direction == "Stade Charléty - Porte de Gentilly (Paris)" and dir1 == 1:
        attentes[1] = attente
        dir1=2
    
    elif direction == "Palais Royal - Musée du Louvre (Paris)" and dir2 == 1:
        attentes[3] = attente
        dir2 = 2


with open("src/data_bus.txt", "a") as data:
    #on ecrit attente + " "
    data.write(str(attentes[0]) + " ")
    data.write(str(attentes[1]) + " ")
    data.write(str(attentes[2]) + " ")
    data.write(str(attentes[3]) + " ")

dir1=0
dir2=0
attentes = [0,0,0,0]
# BUS 63 Cuvier #
for departure in data_req63['departures']:
    heure_passage = departure['stop_date_time']['departure_date_time'].split('T')[1]
    heure_passage = heure_passage[:2] + 'h' + heure_passage[2:4] + 'm' + heure_passage[4:6] + 's'
    direction = departure['display_informations']['direction'] 
    #on affiche ensuite la direction
    print('Direction:', direction)

    
    # pattern de prints de debug
    print('Heure de passage:', heure_passage)

    #on recup l'heure + minute actuelle
    heure_actuelle = time.strftime("%H:%M:%S", time.localtime())
    heure_actuelle = heure_actuelle.split(':')
    minute_actuelle = int(heure_actuelle[1])
    heure_actuelle = int(heure_actuelle[0])
    attente = (int(heure_passage[:2]) - heure_actuelle)*60 + int(heure_passage[3:5]) - minute_actuelle

    if direction == "Gare de Lyon - Maison de la RATP (Paris)" and dir1 == 0:
        dir1=1
        attentes[0] = attente
    elif direction == "Porte de la Muette (Paris)" and dir2 == 0:
        dir2 = 1
        attentes[2] = attente
    
    elif direction == "Gare de Lyon - Maison de la RATP (Paris)" and dir1 == 1:
        attentes[1] = attente
        dir1=2
    
    elif direction == "Porte de la Muette (Paris)" and dir2 == 1:
        attentes[3] = attente
        dir2 = 2


with open("src/data_bus.txt", "a") as data:
    #on ecrit attente + " "
    data.write(str(attentes[0]) + " ")
    data.write(str(attentes[1]) + " ")
    data.write(str(attentes[2]) + " ")
    data.write(str(attentes[3]) + " ")