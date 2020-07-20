import os, json
from Character import Character
from Events import Events
class FileWork:
    @staticmethod
    def LoadCharacters():
        allCharacters = list()
        files = os.listdir("jsons/characters/")
        print("Кол-во файлов персонажей: ", len(files))
        for i in files:
            print('Распаковка файла: ', i)
            f = open("jsons/characters/{}".format(i), "rt")
            jsoned = json.load(f)
            f.close()
            character = Character(jsoned)
            print('Успешно создан персонаж {name} {surname}'.format(name=character.name,surname=character.surname))
            allCharacters.append(character)
        return allCharacters

    @staticmethod
    def LoadEvents():
        print("Загружаем файл событий...")
        eventsFile = open("jsons/events.json","rt")
        allEvents = json.load(eventsFile)
        eventsFile.close()
        events = Events(allEvents)
        print("Было загружено {} актов".format(len(events.acts)))
        return events