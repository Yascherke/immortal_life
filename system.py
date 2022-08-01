#from aiogram.dispatcher.filters.state import State, StatesGroup
from pymongo import MongoClient
from mongodb import Finder

cluster = MongoClient(
    "mongodb+srv://Nere:0662@immortalworld.9ig3g.mongodb.net/immortal?retryWrites=true&w=majority")
db = cluster["immortal"]
users = db["players"]
sects = db["sects"]
cultiv = db["cultivation"]


class System():

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
            users.update_one({"_id": self.uid}, {
                             "$set": {"exp": user[7] - cult['cost']}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"level": user[6] + 1}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"points": user[8] + 5}})
            return True

    def sendExp(self, msg):
        finder = Finder(self.uid)
        getter = msg.replace(' для ', ',').split(',')
        user = finder.findParamByName(getter[1])
        exp = int(getter[0])
        users.update_one({"name": getter[1]}, {"$set": {"exp": user[7] + exp}})

    def regen(self):
        finder = Finder(self.uid)
        param = finder.findUserParamByID()
        user = finder.findUserBodyByID()
        spiritual = finder.findUserSpiritualRootByID()
        regen = param[5]
        lvl = param[6]

        if spiritual[5] >= 5 and spiritual[5] < 30:
            users.update_one({"_id": self.uid}, {
                             "$set": {"head": user[0] + regen + 15}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"torso": user[1] + regen + 15}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"rightArm": user[2] + regen + 15}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"leftArm": user[3] + regen + 15}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"rightLeg": user[4] + regen + 15}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"leftLeg": user[5] + regen + 15}})

            if lvl <= 11 and user[0] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 15
            if lvl > 11 and lvl <= 17 and user[0] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 15
            if lvl > 11 and lvl <= 23 and user[0] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 15

            if lvl <= 11 and user[1] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 15
            if lvl > 11 and lvl <= 17 and user[1] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 15
            if lvl > 11 and lvl <= 23 and user[1] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 15

            if lvl <= 11 and user[2] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 15
            if lvl > 11 and lvl <= 17 and user[2] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 15
            if lvl > 11 and lvl <= 23 and user[2] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 15

            if lvl <= 11 and user[3] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 15
            if lvl > 11 and lvl <= 17 and user[3] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 15
            if lvl > 11 and lvl <= 23 and user[3] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 15

            if lvl <= 11 and user[4] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 15
            if lvl > 11 and lvl <= 17 and user[4] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 15
            if lvl > 11 and lvl <= 23 and user[4] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 15

            if lvl <= 11 and user[5] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 15
            if lvl > 11 and lvl <= 17 and user[5] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 15
            if lvl > 11 and lvl <= 23 and user[5] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 15

            return regen + 15

        elif spiritual[5] >= 30 and spiritual[5] < 60:
            users.update_one({"_id": self.uid}, {
                             "$set": {"head": user[0] + regen + 40}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"torso": user[1] + regen + 40}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"rightArm": user[2] + regen + 40}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"leftArm": user[3] + regen + 40}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"rightLeg": user[4] + regen + 40}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"leftLeg": user[5] + regen + 40}})

            if lvl <= 11 and user[0] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 40
            if lvl > 11 and lvl <= 17 and user[0] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 40
            if lvl > 11 and lvl <= 23 and user[0] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 40

            if lvl <= 11 and user[1] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 40
            if lvl > 11 and lvl <= 17 and user[1] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 40
            if lvl > 11 and lvl <= 23 and user[1] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 40

            if lvl <= 11 and user[2] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 40
            if lvl > 11 and lvl <= 17 and user[2] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 40
            if lvl > 11 and lvl <= 23 and user[2] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 40

            if lvl <= 11 and user[3] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 40
            if lvl > 11 and lvl <= 17 and user[3] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 40
            if lvl > 11 and lvl <= 23 and user[3] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 40

            if lvl <= 11 and user[4] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 40
            if lvl > 11 and lvl <= 17 and user[4] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 40
            if lvl > 11 and lvl <= 23 and user[4] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 40

            if lvl <= 11 and user[5] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 40
            if lvl > 11 and lvl <= 17 and user[5] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 40
            if lvl > 11 and lvl <= 23 and user[5] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 40

            return regen + 40

        elif spiritual[5] >= 60 and spiritual[5] <= 100:
            users.update_one({"_id": self.uid}, {
                             "$set": {"head": user[0] + regen + 80}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"torso": user[1] + regen + 80}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"rightArm": user[2] + regen + 80}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"leftArm": user[3] + regen + 80}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"rightLeg": user[4] + regen + 80}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"leftLeg": user[5] + regen + 80}})

            if lvl <= 11 and user[0] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 80
            if lvl > 11 and lvl <= 17 and user[0] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 80
            if lvl > 11 and lvl <= 23 and user[0] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 80

            if lvl <= 11 and user[1] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 80
            if lvl > 11 and lvl <= 17 and user[1] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 80
            if lvl > 11 and lvl <= 23 and user[1] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 80

            if lvl <= 11 and user[2] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 80
            if lvl > 11 and lvl <= 17 and user[2] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 80
            if lvl > 11 and lvl <= 23 and user[2] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 80

            if lvl <= 11 and user[3] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 80
            if lvl > 11 and lvl <= 17 and user[3] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 80
            if lvl > 11 and lvl <= 23 and user[3] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 80

            if lvl <= 11 and user[4] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 80
            if lvl > 11 and lvl <= 17 and user[4] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 80
            if lvl > 11 and lvl <= 23 and user[4] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 80

            if lvl <= 11 and user[5] > 100:
                users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                return regen + 80
            if lvl > 11 and lvl <= 17 and user[5] > 150:
                users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                return regen + 80
            if lvl > 11 and lvl <= 23 and user[5] > 200:
                users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                return regen + 80

            return regen + 80
        else:
            users.update_one({"_id": self.uid}, {
                             "$set": {"head": user[0] + regen}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"torso": user[1] + regen}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"rightArm": user[2] + regen}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"leftArm": user[3] + regen}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"rightLeg": user[4] + regen}})
            users.update_one({"_id": self.uid}, {
                             "$set": {"leftLeg": user[5] + regen}})
            return regen

    def upgradeSkill(self, msg):
        finder = Finder(self.uid)
        user = finder.findUserParamByID()
        getter = msg.replace(' на ', ',').split(',')
        skill = getter[0]
        count = int(getter[1])
        ma = finder.findUserMartialSkillsByID()
        sr = finder.findUserSpiritualRootByID()
        craft = finder.findUserCraftByID()

        if user[8] >= 0 and user[8] >= count:
            if skill == "Клинок":
                if ma[0] < 100 and count <= 100:
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"blade": ma[0] + count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    points = user[8] - count
                    num = ma[0] + count
                    if num > 100:
                        res = num - 100
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"blade": 100}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False
            if skill == "Копье":
                if ma[1] < 100 and count <= 100:
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"spear": ma[1] + count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    points = user[8] - count
                    num = ma[1] + count
                    if num > 100:
                        res = num - 100
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"spear": 100}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False

            if skill == "Меч":
                if ma[2] < 100 and count <= 100:
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"sword": ma[2] + count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    points = user[8] - count
                    num = ma[2] + count
                    if num > 100:
                        res = num - 100
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"sword": 100}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False

            if skill == "Кулак":
                if ma[3] < 100 and count <= 100:
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"fist": ma[3] + count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    points = user[8] - count
                    num = ma[3] + count
                    if num > 100:
                        res = num - 100
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"fist": 100}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False

            if skill == "Ладонь":
                if ma[4] < 100 and count <= 100:
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"palm": ma[4] + count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    points = user[8] - count
                    num = ma[4] + count
                    if num > 100:
                        res = num - 100
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"palm": 100}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False

            if skill == "Палец":
                if ma[5] < 100 and count <= 100:
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"finger": ma[5] + count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    points = user[8] - count
                    num = ma[5] + count
                    if num > 100:
                        res = num - 100
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"finger": 100}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False

            if skill == "Огонь":
                if sr[0] < 100 and count <= 100:
                    users.update_one({"_id": self.uid}, {
                                     "$sum": {"fire": sr[0] + count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    points = user[8] - count
                    num = sr[0] + count
                    if num > 100:
                        res = num - 100
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"fire": 100}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False

            if skill == "Вода":
                if sr[1] < 100 and count <= 100:
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"water": sr[1] + count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    points = user[8] - count
                    num = sr[1] + count
                    if num > 100:
                        res = num - 100
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"water": 100}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False

            if skill == "Молния":
                if sr[2] < 100 and count <= 100:
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"lightning": sr[2] + count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    points = user[8] - count
                    num = sr[2] + count
                    if num > 100:
                        res = num - 100
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"lightning": 100}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False

            if skill == "Ветер":
                if sr[3] < 100 and count <= 100:
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"wind": sr[3] + count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    points = user[8] - count
                    num = sr[3] + count
                    if num > 100:
                        res = num - 100
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"wind": 100}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False

            if skill == "Земля":
                if sr[4] < 100 and count <= 100:
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"earth": sr[4] + count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    points = user[8] - count
                    num = sr[4] + count
                    if num > 100:
                        res = num - 100
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"earth": 100}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False

            if skill == "Дерево":
                if sr[5] < 100 and count <= 100:
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"wood": sr[5] + count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    points = user[8] - count
                    num = sr[5] + count
                    if num > 100:
                        res = num - 100
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"wood": 100}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False

            if skill == "Свет":
                if sr[6] < 100 and count <= 100:
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"light": sr[6] + count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    points = user[8] - count
                    num = sr[6] + count
                    if num > 100:
                        res = num - 100
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"light": 100}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False

            if skill == "Тьма":
                if sr[7] < 100:
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"dark": sr[7] + count}})
                    points = user[8] - count
                    num = sr[7] + count
                    if num > 100:
                        res = num - 100
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"dark": 100}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False

            if skill == "Алхимия":
                if craft[0] < 50 and count <= 50:
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"alchemy": craft[0] + count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    points = user[8] - count
                    num = craft[0] + count
                    if num > 50:
                        res = num - 50
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"alchemy": 50}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False

            if skill == "Крафтер":
                if craft[1] < 50 and count <= 50:
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"forge": craft[1] + count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    points = user[8] - count
                    num = craft[1] + count
                    if num > 50:
                        res = num - 50
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"forge": 50}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False

            if skill == "Сбор трав":
                if craft[2] < 50 and count <= 50:
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"herbCollection": craft[2] + count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    points = user[8] - count
                    num = craft[2] + count
                    if num > 50:
                        res = num - 50
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"herbCollection": 50}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False

            if skill == "Сбор руды":
                if craft[3] < 50 and count <= 50:
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"mining": craft[3] + count}})
                    users.update_one({"_id": self.uid}, {
                                     "$set": {"points": user[8] - count}})
                    points = user[8] - count
                    num = craft[3] + count
                    if num > 50:
                        res = num - 50
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"mining": 50}})
                        users.update_one({"_id": self.uid}, {
                                         "$set": {"points": points + res}})
                    return True
                else:
                    return False
        else:
            return False
