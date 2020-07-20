import json
class Events:
    def __init__(self, events):
        self.acts = list()
        for i in events["acts"]:
            self.acts.append(i)

    