import fileWork

class main():
    def __init__(self):
        self.characters = fileWork.FileWork.LoadCharacters()
        self.events = fileWork.FileWork.LoadEvents()

    def game(self):
        for thisAct in self.events.acts:
            print("{actName}, {loc}".format(actName=thisAct["actName"],loc=thisAct["location"]))
            for message in thisAct["messages"]:
                for char in self.characters:
                    if char.characterId == message["characterID"]:
                        if message["type"] == "message":
                            char.say(message["message"],message["time"])

                        elif message["type"] == "action":
                            char.act(message["message"])
                    



if __name__ == "__main__":
    m = main()
    m.game()