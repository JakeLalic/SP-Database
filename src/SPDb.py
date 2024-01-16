from SPDbEntry import SPDbEntry
import json

class SPDb:   

    def __init__(self, init=False, dbName='SPDb.csv'):
        print('TODO: __init__')         
        self.dbName = dbName

        self.playerList = []

    def fetch_player(self):
        print('TODO: fetch_player')
        tupleList = []
        for i in self.playerList:
            players = (i.number, i.name, i.position, i.role, i.minutes)
            tupleList.append(players)
        return tupleList

    def insert_player(self, number, name, position, role, minutes):
        print('TODO: insert_player')
        newEntry = SPDbEntry(number=number, name=name, position=position, role=role, minutes=minutes)
        self.playerList.append(newEntry)
        

    def delete_player(self, number):
        print('TODO: delete_player')
        for i in self.playerList:
            if i.number == number:
                self.playerList.remove(i)
        

    def update_player(self, new_name, new_position, new_role, new_minutes, number):
        print('TODO: update_player')
        for i in self.playerList:
            if i.number == number:
                self.playerList.remove(i)
                i = SPDbEntry(number=number, name = new_name, position = new_position, role = new_role, minutes = new_minutes)
                self.playerList.append(i)

    
    def import_csv(self, filename):
        print('TODO: import_csv')
        with open(filename, 'r') as file:
            words = file.readlines()
            words = words[1:]
        for word in words:
            data = word.strip().split(",")
            info = SPDbEntry(data[0], data[1], data[2], data[3], data[4])
            self.playerList.append(info)



    def export_csv(self):
        print('TODO: export_csv') 
        with open(self.dbName, 'w') as file:
            headers = "Number,Player Name,Position,Team Role,Playing Minutes \n"
            file.write(headers)
            for i in self.playerList:
                Data = str(i.number) + "," + i.name + "," + i.position + "," + i.role + "," + i.minutes + "\n"
                file.write(Data)

    
    def export_json(self):
        print('TODO: export_json')
        team = []
        for player in self.playerList:
            playerData = {
                'Number' : player.number,
                'Player Name' : player.name,
                'Position' : player.position,
                'Team Role' : player.role,
                'Playing Minutes' : player.minutes}
            team.append(playerData)
        with open('SPDb.json' , 'w') as file:
            json_string = json.dumps(team, indent=4)
            file.write(json_string)


    def id_exists(self, number):
        for i in self.playerList:
            if i.number == number:
                return True
            else:
                continue
        return False
