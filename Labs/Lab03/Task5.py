import json
try:
    dictionary = {'Ali': 23,'Saad':24,'Salman':15,'Shams':25,'Sadiq':46,'Hammad':23}

    with open(r'text5.json','w') as jsfile:
        json.dump(dictionary,jsfile)
    with open(r'text5.json','r') as jsfile:
        data = json.load(jsfile)
        oldest = max(data.values())

        for person in data:
            if data[person] == oldest:
                print(person)
except FileNotFoundError:
        print("File not Found")
except IOError:
    print("IOError Occured")
except Exception as error:
    print("Unexpected error")
