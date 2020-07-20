class Character:
    def __init__(self, args):
        self.name = args["name"]
        self.surname = args["surname"]
        self.description = args["description"]
        self.characterId = args["characterId"]

    def say(self, message, time):
        print("{time}, {name} {surname}: {message}".format(name=self.name,surname=self.surname,message=message,time=time))

    def act(self,message):
        print("**{name} {surname} {message}**".format(name=self.name,surname=self.surname,message=message))