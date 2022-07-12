from aiogram.dispatcher.filters.state import State, StatesGroup
from pymongo import MongoClient
from mongodb import Finder

cluster = MongoClient(
        "mongodb+srv://Nere:0662@immortalworld.9ig3g.mongodb.net/immortal?retryWrites=true&w=majority")
db = cluster["immortal"]
users = db["players"]
sects = db["sects"]
cultiv = db["cultivation"]

class System(StatesGroup):

    def __init__(self, uid):
        self.uid = uid

    def levelUp(self):
        finder = Finder(self.uid)
        user = finder.findUserParamByID()
        ucult = user[6] + 1
        for cult in cultiv.find({"_id": ucult}):
             print("Cult finder done")

        check = user[7] - cult['cost']

        if user[7] <= cult['cost'] or check <= 0:
            return False
        else:
            users.update_one({"_id": self.uid}, {"$set": {"exp": user[7] - cult['cost']}})
            users.update_one({"_id": self.uid}, {"$set": {"level": user[6] + 1}})
            users.update_one({"_id": self.uid}, {"$set": {"points": user[8] + 5}})
            return True



