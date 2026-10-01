import json 

shipments = {}

with open("shipments.json") as json_file:
    data = json.load(json_file)

    for e in data:
        shipments[e['id']] = e 


def save():
    with open('shipments.json', 'w') as json_file:
        json.dump(list(shipments.values()), json_file)
print(shipments)