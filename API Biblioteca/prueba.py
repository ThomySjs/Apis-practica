import json

with open('datos/socios.json', 'r') as file:
    data = json.load(file)
    print(data[-1]["dni"])